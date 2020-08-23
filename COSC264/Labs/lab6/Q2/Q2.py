import math
def number_fdma_channels (b_hz, g_hz, u_hz):
    return math.floor((b_hz) / (u_hz + g_hz))


print (number_fdma_channels(1000000, 1000, 30000))
