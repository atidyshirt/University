def message_delay (connSetupTime_s, cableLength_km, speedOfLight_kms, messageLength_b, dataRate_bps):
    return (cableLength_km / speedOfLight_kms) * 2 + (messageLength_b / dataRate_bps) + connSetupTime_s

print ("{:.3f}".format(message_delay(0.2, 10000, 200000, 1000000000, 1000000))) # .460


""" 
DELAY

prop = L / S
tran = L / R
"""
