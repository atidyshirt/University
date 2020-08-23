# More complex combinational logic (ENCE260 lecture CA4)
#
# Allan McInnes / 2018-07-18

# Basic combinational logic components
def two_input_gate(truth_table, in1, in2):
    """Return an output found from a truth table."""
    return truth_table[(in1, in2)]

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

def and_gate(in1, in2):
    return two_input_gate(and_table, in1, in2)

def or_gate(in1, in2):
    return two_input_gate(or_table, in1, in2)

def xor_gate(in1, in2):
    return two_input_gate(xor_table, in1, in2)

# Single-bit full adder
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

# Ripple-carry adder
def ripple_carry_4bit_adder(A, B, cin):
    """
    Takes a pair of 4-tuples (representing 4-bit numbers) and a carry
    value as inputs.
    Returns a 5-tuple containing
    1. the binary sum of the inputs (including a 'carry' input)
    2. a 'carry' value that is non-zero if the sum overflows.
    For all tuples, the first element is the MSB.
    """
    # Decompose input tuples
    A3, A2, A1, A0 = A
    B3, B2, B1, B0 = B
    # Perform addition
    s0, c = full_adder(A0, B0, cin)
    s1, c = full_adder(A1, B1, c)
    s2, c = full_adder(A2, B2, c)
    s3, cout = full_adder(A3, B3, c)
    return (s3, s2, s1, s0, cout)

"""
>>> ripple_carry_4bit_adder((0,1,0,0), (0,0,1,1), 0)
(0, 1, 1, 1, 0)
>>> ripple_carry_4bit_adder((0,1,0,0), (0,0,1,1), 1)
(1, 0, 0, 0, 0)
"""

def ripple_carry_4bit_addsub(A, B, sub):
    """
    Takes a pair of 4-tuples (representing 4-bit numbers), and a sub control signal.
    Returns a 5-tuple containing
    1. the binary sum (or difference) of the inputs
    2. a 'carry' value that is non-zero if the sum overflows.
    For all tuples, the first element is the MSB.
    """
    # Decompose input tuples
    A3, A2, A1, A0 = A
    B3, B2, B1, B0 = B
    # Perform addition
    s0, c = full_adder(A0, xor_gate(B0, sub), sub)
    s1, c = full_adder(A1, xor_gate(B1, sub), c)
    s2, c = full_adder(A2, xor_gate(B2, sub), c)
    s3, cout = full_adder(A3, xor_gate(B3, sub), c)
    return (s3, s2, s1, s0, cout)

"""
>>> ripple_carry_4bit_addsub((0,0,1,1), (0,1,0,0), 1)
(1, 1, 1, 1, 0)
"""
