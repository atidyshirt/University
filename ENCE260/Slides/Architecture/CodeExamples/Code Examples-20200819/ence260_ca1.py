# Basic combinational logic, implemented as functions
# and lookup tables.
# This could also be implemented using classes. But combinational
# logic gates don't have state (the output is just a function of
# the input), so we don't really need to construct gate objects.
#
# Allan McInnes / 2018-07-15

def inverter(input):
    """Return the logical complement of the input."""
    return (0 if input == 1 else 1)

def two_input_gate(truth_table, in1, in2):
    """Return an output found from a truth table."""
    return truth_table[(in1, in2)]

# Truth tables for basic logic operations
and_table = {(0,0):0,
             (0,1):0,
             (1,0):0,
             (1,1):1}

or_table =  {(0,0):0,
             (0,1):1,
             (1,0):1,
             (1,1):1}

xor_table = {(0,0):0,
             (0,1):1,
             (1,0):1,
             (1,1):0}

# Basic logic gates
def and_gate(in1, in2):
    return two_input_gate(and_table, in1, in2)

# Test this code with:
# a = 1
# b = 0
# and_gate(a, b)
# b = 1
# and_gate(a, b)


def or_gate(in1, in2):
    return two_input_gate(or_table, in1, in2)

def xor_gate(in1, in2):
    return two_input_gate(xor_table, in1, in2)

# Building more complex operations from the basic gates
def half_adder(in1, in2):
    """
    Returns a 2-tuple containing
    1. the binary sum of the inputs
    2. a 'carry' value that is non-zero if the sum overflows
    """
    return (xor_gate(in1, in2), and_gate(in1, in2))

# half_adder(0,1)

def full_adder(in1, in2, cin):
    """
    Returns a 2-tuple containing
    1. the binary sum of the inputs (including a 'carry' input)
    2. a 'carry' value that is non-zero if the sum overflows.
    """
    s = xor_gate(xor_gate(in1, in2), cin)
    cout = or_gate(or_gate(and_gate(in1, in2),
            and_gate(in1, cin)), and_gate(in2, cin))
    return (s, cout)
