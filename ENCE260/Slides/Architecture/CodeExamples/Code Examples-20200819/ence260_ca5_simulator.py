# Introducing feedback loops into logic circuits (sequential logic) means
# that we need to start considering time in our analysis. A classic way
# to manage time in logic circuit analysis is "discrete-event simulation".
# In a discrete-event simulation we look for changes in the level of signals,
# and keep track of the time at which those changes occur (a "discrete event"
# is thus a pair (time, value change). This allows us to jump from one
# signficant event to the next, instead of trying to compute the values of
# circuit at every instant.
#
# Here you'll find a simple discrete-event logic simulator, loosely based on
# the design found in Abelson & Sussman's "Structure and Interpretation of
# Computer Programs".
#
# The concept:
#   - Components respond to changes at their inputs by producing new outputs
#   - Wires connect outputs from one component to the inputs of other components
#   - The Scheduler manages the order of update events
#
# Relevant to ENCE260 lectures CA3, CA4, and CA5
#
# Allan McInnes / 2018-08-16

# --- Simulation infrastructure ---
class Scheduler:
    """Scheduler executes a simulation by firing scheduled events in time order.
    The simulation time advances in variable steps, jumping from one event
    execution time to the next. This is more efficient and more accurate
    than moving the execution forward in fixed-size steps as a discrete-time
    simulation would do.

    The scheduler maintains a queue of future events, ordered by the time of
    their execution. As events are pulled from the top of the queue and fired,
    the simulation time is advanced. As a result of firing an event, one or
    more new events may be scheduled for the future. The simulation continues
    until no new events are scheduled."""
    def __init__(self):
        self.current_time = 0.0
        self.event_queue = []

    def run(self):
        while len(self.event_queue) > 0:
            event = self.event_queue.pop(0)
            self.current_time = event.time
            # print("{}: {} @ {}".format(event.wire.name, event.value, event.time))
            event.execute()

    def add_event(self, wire, value, dt):
        """This is not an efficient way to manage the list, but it will
        work for this simple demo."""
        event = Event(self.current_time + dt, wire, value)
        index = next((i for i, e in enumerate(self.event_queue) if e.time > event.time), None)
        if index is not None:
            self.event_queue.insert(index, event)
        else:
            self.event_queue.append(event)
        # print("{}: {} @ {}".format(event.wire.name, event.value, event.time))


class Event:
    """An event occurs at a time, and results in a value appearing on a wire."""
    def __init__(self, time, wire, value):
        self.time = time
        self.wire = wire
        self.value = value

    def execute(self):
        self.wire.set_signal(self.value)

# --- Wires ---
class Wire:
    """Connects components via an Observer pattern."""
    def __init__(self, name = "?"):
        self.name = name
        self.signal = 0 # Default value
        self.observers = []

    def add_observer(self, obs):
        self.observers.append(obs)

    def get_signal(self):
        return self.signal

    def set_signal(self, value):
        if not value == self.signal:
            self.signal = value
            for observer in self.observers:
                observer.notify()

class Component:
    """Base class for components."""
    def __init__(self, scheduler, delay):
        self.DELAY = delay
        self.scheduler = scheduler

    def observe_inputs(self, *wires):
        """Set up the component as an observer of all wires."""
        for wire in wires:
            wire.add_observer(self)

    def add_event(self, wire, value):
        """Schedule a new event on the specified wire."""
        self.scheduler.add_event(wire, value, self.DELAY)


# --- Combinational logic ---
class Inverter(Component):
    """Return the logical complement of the input."""
    def __init__(self, scheduler, inp, out):
        super().__init__(scheduler, delay=2.0)
        self.observe_inputs(inp)
        self.inp = inp
        self.out = out

    def notify(self):
        inp = self.inp.get_signal()
        self.add_event(self.out, (0 if inp == 1 else 1))


class TwoInputGate(Component):
    """Generic two-input gate"""
    def __init__(self, scheduler, truth_table, in1, in2, out):
        super().__init__(scheduler, delay=4.0)
        self.observe_inputs(in1, in2)
        self.in1 = in1
        self.in2 = in2
        self.out = out
        self.truth_table = truth_table

    def notify(self):
        in1 = self.in1.get_signal()
        in2 = self.in2.get_signal()
        self.add_event(self.out, self.truth_table[(in1, in2)])


# Truth tables for basic logic operations
and_table = {(0,0):0, (0,1):0, (1,0):0, (1,1):1}
or_table =  {(0,0):0, (0,1):1, (1,0):1, (1,1):1}
xor_table = {(0,0):0, (0,1):1, (1,0):1, (1,1):0}
nor_table = {(0,0):1, (0,1):0, (1,0):0, (1,1):0}

# Basic logic gates
class AndGate(TwoInputGate):
    def __init__(self, scheduler, in1, in2, out):
        super().__init__(scheduler, and_table, in1, in2, out)

class OrGate(TwoInputGate):
    def __init__(self, scheduler, in1, in2, out):
        super().__init__(scheduler, or_table, in1, in2, out)

class XorGate(TwoInputGate):
    def __init__(self, scheduler, in1, in2, out):
        super().__init__(scheduler, xor_table, in1, in2, out)

class NorGate(TwoInputGate):
    def __init__(self, scheduler, in1, in2, out):
        super().__init__(scheduler, nor_table, in1, in2, out)

# --- Sequential logic ---

class SRLatch(Component):
    """Connect NOR gates in an SR Latch configuration."""
    def __init__(self, scheduler, S, R, Q, Qnot):
        # Really just a container for cross-coupled NOR gates
        self.norA = NorGate(scheduler, S, Q, Qnot)
        self.norB = NorGate(scheduler, R, Qnot, Q)
        # Force an evaluation of the initial state
        self.norA.notify()
        self.norB.notify()

    def notify(self):
        # Handled by the component gates
        pass


class DFlipFlop(Component):
    """Simulate behaviour (but not internal construction) of a D Flip Flop."""
    def __init__(self, scheduler, D, Clk, Q, Qnot):
        super().__init__(scheduler, delay=6.0)
        self.observe_inputs(Clk)
        self.D = D
        self.Clk = Clk
        self.Q = Q
        self.Qnot = Qnot
        self.Clk.add_observer(self)
        self.last_clk_level = self.Clk.get_signal()

    def notify(self):
        # Check for rising edge
        if self.last_clk_level == 0 and self.Clk.get_signal() == 1:
            inp = self.D.get_signal()
            self.add_event(self.Q, inp)
            self.add_event(self.Qnot, (0 if inp == 1 else 1))
        self.last_clk_level = self.Clk.get_signal()


# --- Helpers ---
class SignalSensor(Component):
    """Print a signal transition as an output."""
    def __init__(self, scheduler, wire):
        super().__init__(scheduler, delay=0.0)
        self.observe_inputs(wire)
        self.wire = wire

    def notify(self):
        print("{} ns: {} --> {}".format(self.scheduler.current_time,
                                         self.wire.name,
                                         self.wire.get_signal()))

class StateSampler(Component):
    """Print a state value on the rising edge of each clock cycle."""
    def __init__(self, scheduler, clock, *wires):
        super().__init__(scheduler, delay=0.0)
        self.clock = clock
        self.last_clock_level = self.clock.get_signal()
        self.observe_inputs(clock)
        self.wires = wires

    def notify(self):
        # Check for rising edge
        if self.last_clock_level == 0 and self.clock.get_signal() == 1:
            print("State at {} ns".format(self.scheduler.current_time))
            for wire in self.wires:
                print("\t{} = {}".format(wire.name, wire.get_signal()))
        self.last_clock_level = self.clock.get_signal()



def add_clock_signal(scheduler, wire, period, cycles):
    """Put `cycles` periods of a clock with a `period` ns period onto a wire."""
    for cycle in range(1,cycles):
        scheduler.add_event(wire, 1, cycle*period)
        scheduler.add_event(wire, 0, cycle*period + 0.5*period)

# --- Sample usage ---

def simulate_2bit_counter():
    # Simulate a simple 2-bit counter
    print("\nShort run of a 2-bit counter built from D Flip-Flops")
    print("------------------------------------------------------")
    sched = Scheduler()

    # Set up clock signal
    clk = Wire("Clk")
    add_clock_signal(sched, clk, 1000.0, 15)

    # Define wires
    q0 = Wire("Q0")
    q1 = Wire("Q1")
    qnot0 = Wire("Qnot0")
    qnot1 = Wire("Qnot1")
    xor_out = Wire()

    # Build counter from flip-flops
    d1 = DFlipFlop(sched, qnot0, clk, q0, qnot0)
    d2 = DFlipFlop(sched, xor_out, clk, q1, qnot1)
    xor = XorGate(sched, q0, q1, xor_out)

    # Set up output
    out1 = SignalSensor(sched, q0)
    out2 = SignalSensor(sched, q1)
    out3 = StateSampler(sched, clk, q0, q1)

    # Execute the sim
    sched.run()

def simulate_sr_latch():
    # Simulate an SR Latch
    print("\nAn SR Latch built from two NOR gates (note initial oscillation until reset applied)")
    print("------------------------------------------------------")
    sched = Scheduler()

    # Define wires
    s = Wire("S")
    r = Wire("R")
    q = Wire("Q")
    qnot = Wire("Qnot")

    # The latch
    latch = SRLatch(sched, s, r, q, qnot)

    # Set up output
    out1 = SignalSensor(sched, s)
    out2 = SignalSensor(sched, r)
    out3 = SignalSensor(sched, q)
    out4 = SignalSensor(sched, qnot)

    # Put some signals into the Latch
    # 1. Reset the latch at 100 ns
    # 2. Return the reset line to 0 at 120 ns
    # 3. Set the latch at 2000 ns
    # 4. Return the set line to 0 at 2500 ns
    # 5. Reset the latch at 3100 ns
    # 6. Return the reset line to 0 at 4000 ns
    sched.add_event(r, 1, 100.0)
    sched.add_event(r, 0, 120.0)
    sched.add_event(s, 1, 2000.0)
    sched.add_event(s, 0, 2500.0)
    sched.add_event(r, 1, 3100.0)
    sched.add_event(r, 0, 4000.0)

    # Execute the sim
    sched.run()

def simulate_tut2_sr_latch():
    # Simulate an SR Latch
    print("\nSimulate the SR Latch scenario from tutorial #2")
    print("------------------------------------------------------")
    sched = Scheduler()

    # Define wires
    s = Wire("S")
    r = Wire("R")
    q = Wire("Q")
    qnot = Wire("Qnot")

    # The latch
    latch = SRLatch(sched, s, r, q, qnot)

    # Set up output
    out1 = SignalSensor(sched, s)
    out2 = SignalSensor(sched, r)
    out3 = SignalSensor(sched, q)
    out4 = SignalSensor(sched, qnot)

    # Put some signals into the Latch
    # A. Establish a reset state (Q = 0, notQ = 1)
    # 1. Reset the latch at 100 ns
    # 2. Return the reset line to 0 at 120 ns
    sched.add_event(s, 0, 1.0)
    sched.add_event(r, 1, 1.0)
    sched.add_event(r, 0, 20.0)
    # Set up inputs for S = 1 and R = 0 (note that R is already 0)
    sched.add_event(s, 1, 100.0)
    sched.add_event(r, 0, 100.0)

    # Execute the sim
    sched.run()


if __name__ == "__main__":
    simulate_sr_latch()
    simulate_2bit_counter()
    simulate_tut2_sr_latch()
