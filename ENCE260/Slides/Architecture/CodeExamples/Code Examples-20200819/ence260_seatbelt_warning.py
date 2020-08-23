# Simple combinational logic design for
# running a seatbelt warning light.
#
# Example inspired by Frank Vahid's "Digital Design" (Wiley, 2007)
#
# Allan McInnes / 2018-07-23

from ence260_ca1 import inverter, and_gate, or_gate

def seatbelt_warning(is_speed_above_0, is_buckled):
    """
    If the speed is above zero and the seatbelt is not buckled
    the warning should be on
    """
    return and_gate(is_speed_above_0, inverter(is_buckled))
"""
>>> for buckled in (0,1):
...   for speed in (0,1):
...     w = seatbelt_warning(speed, buckled)
...     print("{} {} | {}".format(buckled, speed, w))
...
0 0 | 0
0 1 | 1
1 0 | 0
1 1 | 0
"""

def seatbelt_warning_with_passenger(is_speed_above_0, is_buckled, passenger_present):
    """
    Extend the seatbelt warning for the passenger seat (only warn when passenger
    isn't present)
    """
    return and_gate(passenger_present, seatbelt_warning(is_speed_above_0, is_buckled))

def seatbelt_warning_with_passenger_and_ignition(is_speed_above_0, is_buckled, passenger_present, is_ignition):
    """Extend seatbelt warning to illuminate when is_ignition (which is 1 for first 5 seconds of key being
       turned) is high. This covers the case where the car warning lights illuminate when the care
       is started.
    """
    return or_gate(is_ignition,
                   seatbelt_warning_with_passenger(is_speed_above_0,
                                                   is_buckled,
                                                   passenger_present))
"""
>>> for b in (0,1):
...   for s in (0,1):
...     for p in (0,1):
...       for i in (0,1):
...         w = seatbelt_warning_with_passenger_and_ignition(s, b, p, i)
...         print("{} {} {} {} | {}".format(b, s, p, i, w))
... 
0 0 0 0 | 0
0 0 0 1 | 1
0 0 1 0 | 0
0 0 1 1 | 1
0 1 0 0 | 0
0 1 0 1 | 1
0 1 1 0 | 1
0 1 1 1 | 1
1 0 0 0 | 0
1 0 0 1 | 1
1 0 1 0 | 0
1 0 1 1 | 1
1 1 0 0 | 0
1 1 0 1 | 1
1 1 1 0 | 0
1 1 1 1 | 1
"""
