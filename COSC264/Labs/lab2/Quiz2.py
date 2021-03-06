def _transmission_delay(packetLength_bytes, rate_mbps):
    MEGABITS_TO_BYTES = 125000
    return packetLength_bytes / rate_mbps / MEGABITS_TO_BYTES

#  print ("{:.3f}".format(transmission_delay(1000000, 4)))

def transmission_delay (packetLength_bytes, rate_bps):
    return packetLength_bytes / rate_bps * 8

#  print ("{:.3f}".format(transmission_delay(1000000, 4000000)))

def total_time (cableLength_KM, packetLength_b):
     SOL = 200000 #KM/s
     RATE = 10 #Gbps

#  print ("{:.4f}".format(total_time(10000, 8000)))

def queueing_delay (rate_bps, numPackets, packetLength_b):
    return packetLength_b / rate_bps * numPackets

#  print ("{:.3f}".format(queueing_delay(100*125000, 20, 1500*8)))

def per_from_ber (bitErrorProb, packetLen_b):
    return 1-((1-bitErrorProb)**packetLen_b)

def avg_trials_from_ber (bit_error_probability, packetLength_b):
    prob = per_from_ber(bit_error_probability, packetLength_b)
    return 1 + prob/(1-prob)

print ("{:.3f}".format(avg_trials_from_ber(0.0001, 1000)))

