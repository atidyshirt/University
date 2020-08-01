def connection_setup_delay (cableLength_km, speedOfLight_kms, dataRate_bps, messageLength_b, processingTimes_s):
    return (messageLength_b/dataRate_bps) * (cableLength_km/speedOfLight_kms) * processingTimes_s

print ("{:.4f}".format(connection_setup_delay(10000, 200000, 1000000, 1000, 0.001)))
