# Small simulator for a simple register machine.
#
# Allan McInnes / 2018-09-17
# 0.1.0 - Initial version
# 0.1.1 - Bugfixes to DEBUG_OUT output

"""The MicroC simulator is a behavioural model of a microcontroller
that allows you to experiment with executing small assembly
language programs.

The model is of a Harvard-style architecture, since it has separate
program and data memories. The instruction set is RISC-like, and
loosely based on AVR instructions. Instructions are stored as
assembly-style strings rather than as binary, since this keeps
the simulator simple.

A program is executed by fetching an instruction from the program
memory address currently contained in the Program Counter register,
"decoding" the instruction to determine the operation and operands,
and "executing" the instruction by invoking the appropriate
instruction set function.

* Running Programs
Having instantiated a MicroC object, programs can be loaded into the
program memory using the `load_program()` method, which accepts a
list of strings as an argument. The currently  loaded program is
executed by invoking the `run()` method with no arguments.
Alternatively, a program can be loaded and run in one step
by passing the program to `run()`.
"""

VERSION = "0.1.1"

import math
import operator
import sys
import os
import getopt
import unittest

class Memory:
    """A simple memory component that offers reads and writes."""
    def __init__(self, size):
        self._memory = [0 for i in range(size)]

    def write(self, address, data):
        self._memory[address] = data

    def read(self, address):
        return self._memory[address]

    def as_strings(self):
        return ["{}: '{}'".format(addr, val) for addr, val in enumerate(self._memory)]


class MicroC:
    """Simulate a simple register machine."""
    PROGRAM_MEM_SIZE = 128
    DATA_MEM_SIZE = 256
    GPR_FILE_SIZE = 8
    WORDSIZE_BIT_MASK = 0xFFFF # Restrict to 16-bit ints
    COMMENT_DELIMITER = ';'

    def __init__(self):
        self._exec_log = ""
        # Set up instruction set (loosely based on AVR instructions)
        self._instruction_set = {}
        self._instruction_set['DEBUG_OUT'] = self._instr_debug_output
        self._instruction_set['HALT'] = self._instr_halt
        self._instruction_set['CLEAR_N'] = self._instr_clear_neg
        self._instruction_set['CLEAR_Z'] = self._instr_clear_zero
        self._instruction_set['CLEAR_C'] = self._instr_clear_carry
        self._instruction_set['CLEAR_O'] = self._instr_clear_overflow
        self._instruction_set['IN'] = self._instr_read_from_special
        self._instruction_set['OUT'] = self._instr_write_to_special
        self._instruction_set['MOVE'] = self._instr_move
        self._instruction_set['LOAD'] = self._instr_load
        self._instruction_set['LOAD_IMMED'] = self._instr_load_immediate
        self._instruction_set['LOAD_INDIR'] = self._instr_load_indirect
        self._instruction_set['STORE'] = self._instr_store
        self._instruction_set['STORE_IMMED'] = self._instr_store_immediate
        self._instruction_set['STORE_INDIR'] = self._instr_store_indirect
        self._instruction_set['PUSH'] = self._instr_stack_push
        self._instruction_set['POP'] = self._instr_stack_pop
        self._instruction_set['ADD'] = self._instr_alu_add
        self._instruction_set['ADD_IMMED'] = self._instr_alu_add_immediate
        self._instruction_set['SUB'] = self._instr_alu_subtract
        self._instruction_set['SUB_IMMED'] = self._instr_alu_subtract_immediate
        self._instruction_set['AND'] = self._instr_alu_and
        self._instruction_set['OR'] = self._instr_alu_or
        self._instruction_set['XOR'] = self._instr_alu_xor
        self._instruction_set['NOT'] = self._instr_alu_not
        self._instruction_set['CALL'] = self._instr_call
        self._instruction_set['RET'] = self._instr_return
        self._instruction_set['BR_IF_NEG'] = self._instr_branch_if_negative
        self._instruction_set['BR_IF_Z'] = self._instr_branch_if_zero

        # Initialize components
        self._program_memory = Memory(self.PROGRAM_MEM_SIZE)
        self._data_memory = Memory(self.DATA_MEM_SIZE)
        self._register = {'R' + str(i): 0 for i in range(self.GPR_FILE_SIZE)}
        self._special_reg = {'PC':0, 'SP':0, 'STATUS':{}, 'INSTR':None}
        self.reset()

    def get_system_config_as_string(self):
        conf = ""
        conf += "Number of General Registers: {}\n".format(self.GPR_FILE_SIZE)
        conf += "Special Registers: {}\n".format(list(self._special_reg))
        conf += "Program Memory Size: {} instructions\n".format(self.PROGRAM_MEM_SIZE)
        conf += "Data Word Size: {} bits\n".format(round(math.log(self.WORDSIZE_BIT_MASK, 2)))
        conf += "Data Memory Size: {} words\n".format(self.DATA_MEM_SIZE)
        return conf

    def get_instruction_set_as_string(self):
        setstr = ""
        setstr += "Basic syntax: [name] <target>, <source>.\n"
        setstr += "Some instructions have no operands. Others have a target but no source.\n"
        setstr += "Comments are begun using '{}', and continue to the end of the line.\n\n".format(self.COMMENT_DELIMITER)
        for instr, func in self._instruction_set.items():
            setstr += "{} - {}\n".format(instr, func.__doc__)
        return setstr

    def reset(self):
        """Reset the processor state."""
        self._op = None
        self._halted = False
        self._special_reg['PC'] = 0
        self._special_reg['SP'] = self.DATA_MEM_SIZE - 1
        self._special_reg['STATUS'] = {'Neg':False, 'Zero':False}
        self._special_reg['INSTR'] = None

    def load_program(self, program):
        """Load a program, made up of list of instruction strings, into
        program memory for execution."""
        address = 0
        for line in program:
            # Strip comments, convert to upper case, and remove commas
            instr = line.rsplit(self.COMMENT_DELIMITER)[0].strip().upper().replace(',',' ')
            if len(instr) > 0:
                self._program_memory.write(address, instr)
                address += 1

    def get_special_registers(self):
        return self._special_reg

    def get_general_registers(self):
        return self._register

    def get_log(self):
        return self._exec_log

    def run(self, program=None):
        """Execute a program, or whatever is currently in program memory."""
        if program is not None:
            self.load_program(program)
        self.reset()
        while not self._halted:
            self.fetch()
            self.decode()
            self.execute()

    def fetch(self):
        """Fetch the next instruction from program memory."""
        try:
            self._special_reg['INSTR'] = self._program_memory.read(self._special_reg['PC'])
            self._exec_log += "{}: {}\n".format(self._special_reg['PC'], self._special_reg['INSTR'])
            self._special_reg['PC'] += 1
        except IndexError:
            self._halted = True

    def decode(self):
        """Decode the current instruction."""
        self._op = None
        self._target = None
        self._source = None
        if isinstance(self._special_reg['INSTR'], str):
            try:
                decoded = self._special_reg['INSTR'].split()
                self._op = decoded[0]
                if len(decoded) > 1:
                    self._target = decoded[1]
                    if len(decoded) > 2:
                        self._source = decoded[2]
            except:
                self._op = None

    def execute(self):
        """Execute the current instructions."""
        if self._op in self._instruction_set:
            self._instruction_set[self._op]()
        else:
            self._halted = True
            self._exec_log += "Unknown instruction!\n"

    def _string_to_dataword(self, string):
        """Convert string to int, while preserving sign."""
        val = int(string, 0)
        sign = -1 if val < 0 else 1
        word = sign * (abs(val) & self.WORDSIZE_BIT_MASK)
        return word

    def _stack_push(self, value):
        self._data_memory.write(self._special_reg['SP'], value)
        self._special_reg['SP'] -= 1 # Post-decrement stack pointer

    def _stack_pop(self):
        self._special_reg['SP'] += 1 # Pre-increment stack pointer
        return self._data_memory.read(self._special_reg['SP'])

    # Instruction Set
    def _instr_debug_output(self):
        """Print the current state of the specified memory or registers (prog, data, spec, gpr)."""
        if self._target == 'PROG':
            print("-- Program Memory --")
            print(self._program_memory.as_strings())
        elif self._target == 'DATA':
            print("-- Data Memory --")
            print(self._data_memory.as_strings())
        elif self._target == 'SPEC':
            print("-- Special Registers --")
            print(self._special_reg.items())
        elif self._target == 'GPR':
            print("-- General Purpose Registers --")
            print(self._register.items())

    def _instr_halt(self):
        """Stop execution."""
        self._halted = True

    def _instr_clear_neg(self):
        """Clear the 'negative' flag (set it to false)."""
        self._special_reg['STATUS']['Neg'] = False

    def _instr_clear_zero(self):
        """Clear the 'zero' flag (set it to false)."""
        self._special_reg['STATUS']['Zero'] = False

    def _instr_clear_carry(self):
        """Clear the 'carry' flag (set it to false)."""
        self._special_reg['STATUS']['Carry'] = False

    def _instr_clear_overflow(self):
        """Clear the 'overflow' flag (set it to false)."""
        self._special_reg['STATUS']['Overflow'] = False

    def _instr_read_from_special(self):
        """Read from a special register into <target>. If <source> is 'PORT' then read from console."""
        if self._source == 'PORT':
            self._register[self._target] = self._string_to_dataword(input('Input?'))
        else:
            self._register[self._target] = self._special_reg[self._source]

    def _instr_write_to_special(self):
        """Write from <source> to a special register. If <target> is 'PORT' then write to console."""
        if self._target == 'PORT':
            print("{}".format(self._register[self._source]))
        else:
            self._special_reg[self._target] = self._register[self._source]

    def _instr_stack_push(self):
        """Push <target> register onto stack."""
        self._stack_push(self._register[self._target])

    def _instr_stack_pop(self):
        """Pop from stack into <target> register."""
        self._register[self._target] = self._stack_pop()

    # Data transfer
    def _instr_move(self):
        """Copy value from <source> to <target>."""
        self._register[self._target] = self._register[self._source]

    def _instr_load(self):
        """Load data from <source> address into <target> register."""
        self._register[self._target] = \
            self._data_memory.read(self._string_to_dataword(self._source))

    def _instr_load_immediate(self):
        """Load literal <source> value into <target> register."""
        self._register[self._target] = self._string_to_dataword(self._source)

    def _instr_load_indirect(self):
        """Load data from address contained in <source> register into <target> register (may include numeric address offset following '+')."""
        indirection = self._source.split('+')
        address = self._register[indirection[0]]
        if len(indirection) > 1:
            address += self._string_to_dataword(indirection[1])
        self._register[self._target] = self._data_memory.read(address)

    def _instr_store(self):
        """Store data from <source> to <target> address."""
        self._data_memory.write(self._string_to_dataword(self._target),
                                self._register[self._source])

    def _instr_store_immediate(self):
        """Store literal <source> value to <target> address."""
        self._data_memory.write(self._string_to_dataword(self._target),
                                self._string_to_dataword(self._source))

    def _instr_store_indirect(self):
        """Store data from <source> register to address contained in <target> register (may include numeric address offset following '+')."""
        indirection = self._target.split('+')
        address = self._register[indirection[0]]
        if len(indirection) > 1:
            address += self._string_to_dataword(indirection[1])
        self._data_memory.write(address, self._register[self._source])

    # Arithmetic/logical -- these would be carried out by the ALU
    def _alu_arithmetic_status(self, result):
        self._instr_clear_neg()
        self._instr_clear_zero()
        self._instr_clear_carry()
        self._instr_clear_overflow()
        if result == 0:
            self._special_reg['STATUS']['Zero'] = True
        if result < 0:
            self._special_reg['STATUS']['Neg'] = True
        if result > self.WORDSIZE_BIT_MASK:
            self._special_reg['STATUS']['Carry'] = True
        if abs(result) > self.WORDSIZE_BIT_MASK/2:
            self._special_reg['STATUS']['Overflow'] = True

    def _alu_logical_status(self, result):
        self._instr_clear_neg()
        self._instr_clear_zero()
        self._instr_clear_carry()
        self._instr_clear_overflow()
        if result == 0:
            self._special_reg['STATUS']['Zero'] = True

    def _alu_arithmetic_op(self, op, target, source):
        result = op(target, source)
        sign = -1 if result < 0 else 1
        self._alu_arithmetic_status(result)
        result = sign * (abs(result) & self.WORDSIZE_BIT_MASK)
        return result

    def _alu_logical_op(self, op, target, source):
        result = op(target, source) & self.WORDSIZE_BIT_MASK
        self._alu_logical_status(result)
        return result

    def _instr_alu_add(self):
        """Add <source> to <target> and save result in <target>."""
        self._register[self._target] = \
            self._alu_arithmetic_op(operator.add,
                self._register[self._target], self._register[self._source])

    def _instr_alu_add_immediate(self):
        """Add literal <source> value to <target> and save result in <target>."""
        self._register[self._target] = \
            self._alu_arithmetic_op(operator.add,
                self._register[self._target], self._string_to_dataword(self._source))

    def _instr_alu_subtract(self):
        """Subtract <source> from <target> and save result in <target>."""
        self._register[self._target] = \
            self._alu_arithmetic_op(operator.sub,
                self._register[self._target], self._register[self._source])

    def _instr_alu_subtract_immediate(self):
        """Subtract literal <source> value from <target> and save result in <target>."""
        self._register[self._target] = \
            self._alu_arithmetic_op(operator.sub,
                self._register[self._target], self._string_to_dataword(self._source))

    def _instr_alu_and(self):
        """Bitwise AND <source> and <target>, save result to <target>."""
        self._register[self._target] = \
            self._alu_logical_op(operator.and_,
                self._register[self._target], self._register[self._source])

    def _instr_alu_or(self):
        """Bitwise OR <source> and <target>, save result to <target>."""
        self._register[self._target] = \
            self._alu_logical_op(operator.or_,
                self._register[self._target], self._register[self._source])

    def _instr_alu_xor(self):
        """Bitwise XOR <source> and <target>, save result to <target>."""
        self._register[self._target] = \
            self._alu_logical_op(operator.xor,
                self._register[self._target], self._register[self._source])

    def _instr_alu_not(self):
        """Bitwise NOT <target>, save result to <target>."""
        result = operator.invert(self._register[self._target]) & self.WORDSIZE_BIT_MASK
        self._alu_logical_status(result)
        self._register[self._target] = result

    # Branching
    def _instr_call(self):
        """Save current PC to stack, and set PC to <target>."""
        self._stack_push(self._special_reg['PC'])
        self._special_reg['PC'] = self._string_to_dataword(self._target)

    def _instr_return(self):
        """Set PC to current top-of-stack value."""
        self._special_reg['PC'] = self._stack_pop()

    def _instr_branch_if_negative(self):
        """Add <target> to PC if 'negative' flag set.
        Note that PC will have been incremented prior to the branch instruction executing."""
        if self._special_reg['STATUS']['Neg']:
            self._special_reg['PC'] += self._string_to_dataword(self._target)

    def _instr_branch_if_zero(self):
        """Add <target> to PC if 'zero' flag set.
        Note that PC will have been incremented prior to the branch instruction executing."""
        if self._special_reg['STATUS']['Zero']:
            self._special_reg['PC'] += self._string_to_dataword(self._target)


# --- Built-in self-tests
class TestMicroC(unittest.TestCase):
    """Suite of simple unit tests for the MicroC simulator."""
    def setUp(self):
        self._machine = MicroC()

    def testComments(self):
        """Comments should be parsed, but ignored."""
        self._machine.run(["store_immed 1, 45 ; A comment",
                           " ; An empty line",
                           "load r0, 1",
                           ";"])
        gpr = self._machine.get_general_registers()
        self.assertEqual(45, gpr['R0'])

    def testSimpleArithmetic(self):
        """Simple arithmetic operations."""
        self._machine.run(["load_immed r1, 10",
                           "load_immed r2, 5",
                           "add r1, r2",
                           "add_immed r1, 3",
                           "load_immed r3, 2",
                           "sub r2, r3",
                           "sub_immed r2, 7"])
        gpr = self._machine.get_general_registers()
        spr = self._machine.get_special_registers()
        self.assertEqual(18, gpr['R1'])
        self.assertEqual(-4, gpr['R2'])
        self.assertEqual(False, spr['STATUS']['Zero'])
        self.assertEqual(True, spr['STATUS']['Neg'])
        self.assertEqual(False, spr['STATUS']['Carry'])
        self.assertEqual(False, spr['STATUS']['Overflow'])

    def testCarryAndOverflow(self):
        """Arithemetic may chnage the status registers."""
        self._machine.run(["load_immed r1, 0xFFFE",
                           "load_immed r2, 0x0003",
                           "add r1, r2"])
        spr = self._machine.get_special_registers()
        self.assertEqual(False, spr['STATUS']['Zero'])
        self.assertEqual(False, spr['STATUS']['Neg'])
        self.assertEqual(True, spr['STATUS']['Carry'])
        self.assertEqual(True, spr['STATUS']['Overflow'])

    def testLogic(self):
        """Basic logic operations."""
        self._machine.run(["load_immed r1, 0x00F1",
                           "load_immed r2, 0x001F",
                           "load_immed r3, 0x0FF0",
                           "load_immed r4, 0x0010",
                           "load_immed r5, 0x0000",
                           "and r1, r2",
                           "or r2, r3",
                           "xor r4, r1",
                           "not r3",
                           "and r5, r1"])
        gpr = self._machine.get_general_registers()
        spr = self._machine.get_special_registers()
        self.assertEqual(0x11, gpr['R1'])
        self.assertEqual(0x0FFF, gpr['R2'])
        self.assertEqual(0xF00F, gpr['R3'])
        self.assertEqual(0x01, gpr['R4'])
        self.assertEqual(0x00, gpr['R5'])
        self.assertEqual(True, spr['STATUS']['Zero'])
        self.assertEqual(False, spr['STATUS']['Neg'])
        self.assertEqual(False, spr['STATUS']['Carry'])
        self.assertEqual(False, spr['STATUS']['Overflow'])

    def testStoreLoad(self):
        """Values stored to a memory address should be loaded from those
        addresses."""
        self._machine.run(["store_immed 23, 45",
                           "store_immed 24, 57",
                           "load r0, 23",
                           "load r1, 24"])
        gpr = self._machine.get_general_registers()
        self.assertEqual(45, gpr['R0'])
        self.assertEqual(57, gpr['R1'])

    def testBranch(self):
        """Branching should modify the PC."""
        self._machine.run(["load_immed r1, 5",
                           "load_immed r2, 10",
                           "sub r1, r2",
                           "br_if_neg 5"])
        spr = self._machine.get_special_registers()
        # Branch is at address 3. PC will be incremented prior to adding
        # branch amount, and incremented a second time during fetch of the
        # empty instruction that halts machine.
        # Thus PC = 3 + 1 + 5 + 1 = 10
        self.assertEqual(10, spr['PC'])

    def testCall(self):
        """Calling should modify the PC and create a new stack frame."""
        self._machine.run(["load_immed r1, 5",
                           "load_immed r2, 0",
                           "call 0x04",
                           "load_immed r2, 0xDEED",
                           "load_immed r3, 0xFEED",
                           "load r4, 255"]) # Put stack value in r4
        gpr = self._machine.get_general_registers()
        spr = self._machine.get_special_registers()
        self.assertEqual(5, gpr['R1'])
        self.assertEqual(0, gpr['R2'])  # should have skipped 0xDEED line
        self.assertEqual(0xFEED, gpr['R3'])
        self.assertEqual(0x03, gpr['R4'])  # Return address
        self.assertEqual(0x07, spr['PC'])  # PC incremented on halt
        self.assertEqual(0xFE, spr['SP'])  # Stack pointer decremented

    def testRet(self):
        """Returning should modify the PC based on the stack value."""
        self._machine.run(["load_immed r1, 0x04",
                           "push r1 ; Fake PC in stack frame",
                           "ret",
                           "load_immed r2, 0xDEED",
                           "load_immed r3, 0xFEED"])
        gpr = self._machine.get_general_registers()
        spr = self._machine.get_special_registers()
        self.assertEqual(4, gpr['R1'])
        self.assertEqual(0, gpr['R2'])  # should have skipped 0xDEED line
        self.assertEqual(0xFEED, gpr['R3'])
        self.assertEqual(0x06, spr['PC'])  # PC incremented on halt
        self.assertEqual(0xFF, spr['SP'])  # Stack pointer incremented

# --- Startup and arg processing

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def print_basic_usage(scriptname):
    script = os.path.basename(scriptname)
    print("Version {} of a simple microcontroller model, implemented in Python.".format(VERSION))
    print("Usage: python3 {} [options] [program-file]".format(script))
    print("Options:")
    print("\t--help\t\tDisplay more detailed documentation")
    print("\t--verbose\tPrint the sequence of executed instructions")
    print("\t--test\t\tRun unit-tests on the machine")

def print_detailed_help(scriptname):
    print_basic_usage(scriptname)
    mc = MicroC()
    print("")
    print(__doc__)
    print("")
    print("--- Simulator Configuration ---")
    print(mc.get_system_config_as_string())
    print("")
    print("--- Instruction Set ---")
    print(mc.get_instruction_set_as_string())


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            verbosity = False
            opts, args = getopt.getopt(argv[1:], "h", ["help",
                                                       "verbose",
                                                       "test"])
            for opt, param in opts:
                if opt == '--help':
                    print_detailed_help(argv[0])
                    return 1
                elif opt == '--verbose':
                    verbosity = True
                elif opt == '--test':
                    loader = unittest.TestLoader()
                    suite = loader.loadTestsFromTestCase(TestMicroC)
                    unittest.TextTestRunner(verbosity=2).run(suite)
                    return 1

            if len(args) > 0:
                prog = open(args[0])
                mc = MicroC()
                if verbosity:
                    print("--- Simulator Configuration ---")
                    print(mc.get_system_config_as_string())
                    print("--- Program I/O ---")
                mc.run(program=prog.readlines())
                if verbosity:
                    print("--- Sequence of Executed Instructions ---")
                    print(mc.get_log())
            else:
                print_basic_usage(argv[0])
                return 1
        except getopt.GetoptError as err:
             raise Usage(err.msg)

    except Usage as err:
        print(err.msg, file=sys.stderr)
        print("for help use --help", file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
