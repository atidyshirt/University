def queueingDelay(
    packetSize_bits, dataRate_bps, flagCurrentTransmission, numberInQueue
):
    # queue time = (L / R) * N
    L = packetSize_bits
    R = dataRate_bps
    flag = flagCurrentTransmission
    N = numberInQueue
    if flag == False:
        return N * (L / R)
    else:
        return N * (L / R) + (L / R)


print(abs(queueingDelay(1000, 1000000, True, 0) - 0.0005) < 0.00001)
print(abs(queueingDelay(1000, 1000000, False, 0) - 0.0000) < 0.00001)
