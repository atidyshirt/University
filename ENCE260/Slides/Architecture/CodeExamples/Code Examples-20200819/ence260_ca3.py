# Modeling latches and flip-flops(ENCE260 lecture CA3)
#
# Allan McInnes / 2018-07-18

# Repeat definition from CA1
def two_input_gate(truth_table, in1, in2):
    """Return an output found from a truth table."""
    return truth_table[(in1, in2)]

# Build a NOR gate for use in constructing SR latch
nor_table = {(0,0):1,
             (0,1):0,
             (1,0):0,
             (1,1):0}

def nor_gate(in1, in2):
    return two_input_gate(nor_table, in1, in2)

# This obviously won't work, because y and z are undefined:
"""
def sr_latch(s, r):
    y = nor_gate(s, z)
    z = nor_gate(r, y)
    return (y, z)

>>> sr_latch(1,0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in sr_latch
UnboundLocalError: local variable 'z' referenced before assignment
"""

# This version will work (but be careful with making the initial input 0,0).
# It stores the previous internal state, and iterates the internal state
# until that state stabilizes.
#
# Note that this implementation ignores *propagation delay* in the
# logic gates, and hides changes in the outputs until the state
# has stabilized. It's therefore unlikely to be a useful component in building
# larger assemblies of sequential logic components. In practice digital
# logic simulations are implemented using some form of *discrete event simulation*.
#
class SR_Latch:
    def __init__(self):
        self.y = 0
        self.z = 0

    def input(self, s, r):
        new_y, new_z = self._update(s, r)
        while not (self.y, self.z) == (new_y, new_z):
            # Show how the internal state changes
            print("Internal state: {}, {}".format(self.y, self.z))
            self.y, self.z = new_y, new_z
            new_y, new_z = self._update(s, r)

    def output(self):
        return (self.y, self.z)

    def _update(self, s, r):
        return nor_gate(s, self.z), nor_gate(r, self.y)
"""
>>> latch = SR_Latch()
>>> latch.input(1,0)
Internal state: 0, 0
>>> latch.output()
(0, 1)
>>> latch.input(0,1)
Internal state: 0, 1
Internal state: 0, 0
>>> latch.output()
(1, 0)
>>> latch.output()
(1, 0)
>>> latch.input(1,0)
Internal state: 1, 0
Internal state: 0, 0
>>> latch.output()
(0, 1)
"""

# A D flip-flop is essentially just a 1-bit storage component.
# The value it stores changes on each clock.
class D_FlipFlop:
    def __init__(self):
        self.D = 0
        self.Q = 0
        self.notQ = 1

    def input(self, d):
    	self.D = d

    def clock_rising_edge(self):
        """We'll assume an edge-triggered flip-flop for this example."""
        self.Q = self.D  # Capture current input state
        self.notQ = 0 if self.Q == 1 else 1

    def output(self):
        return (self.Q, self.notQ)

"""
>>> dff = D_FlipFlop()
>>> dff.output()
(0, 1)
>>> dff.input(1)
>>> dff.output()
(0, 1)
>>> dff.output()
(0, 1)
>>> dff.clock_rising_edge()
>>> dff.output()
(1, 0)
>>> dff.input(0)
>>> dff.output()
(1, 0)
>>> dff.clock_rising_edge()
>>> dff.output()
(0, 1)
>>> dff.output()
(0, 1)
"""
