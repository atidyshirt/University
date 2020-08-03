def connection_setup_delay (cableLength_km, speedOfLight_kms, dataRate_bps, messageLength_b, processingTimes_s):
    return (cableLength_km + speedOfLight_kms + dataRate_bps + messageLength_b) * 0.001

print ("{:.4f}".format(connection_setup_delay(10000, 200000, 1000000, 1000, 0.001)))
