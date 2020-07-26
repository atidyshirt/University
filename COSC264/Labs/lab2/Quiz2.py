def _transmission_delay(packetLength_bytes, rate_mbps):
    MEGABITS_TO_BYTES = 125000
    return packetLength_bytes / rate_mbps / MEGABITS_TO_BYTES

#  print ("{:.3f}".format(transmission_delay(1000000, 4)))

def transmission_delay (packetLength_bytes, rate_bps):
    return packetLength_bytes / rate_bps * 8

#  print ("{:.3f}".format(transmission_delay(1000000, 4000000)))
