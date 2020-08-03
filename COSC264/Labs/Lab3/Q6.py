import math
def total_number_bits (maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b, messageLength_b):
    S = maxUserDataBitsPerPacket_b # number of user data bits
    O = overheadBitsPerPacket_b # number of extra bits (header and trail)
    M = messageLength_b # len
    return S + M + O
print ("{:.1f}".format(total_number_bits(1000, 100, 10000))) # = 11000
