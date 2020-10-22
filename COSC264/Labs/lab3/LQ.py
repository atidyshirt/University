def total_transfer_time (linkLength_km, speedOfLight_kms, processingDelay_s, dataRate_bps, maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b, messageLength_b):
    l = linkLength_km
    c = speedOfLight_kms
    p = processingDelay_s
    r = dataRate_bps
    s = maxUserDataBitsPerPacket_b
    o = overheadBitsPerPacket_b
    m = messageLength_b
    return (2*l/c) + (2*p) + (2*((s+o)/r) + ((m/s)-1) * max(((s+o)/r), p))

print(total_transfer_time(10000, 200000, 0.001, 1000000, 1000, 100, 1000000000))
