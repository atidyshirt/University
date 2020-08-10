import math
def number_fragments (messageSize_bytes, overheadPerPacket_bytes, maximumNPacketSize_bytes):
    s = messageSize_bytes
    o = overheadPerPacket_bytes
    m = maximumNPacketSize_bytes
    return math.ceil(((((s + (o * ((s + o) / m))) / m))))

def last_fragment_size (messageSize_bytes, overheadPerPacket_bytes, maximumNPacketSize_bytes):
    s = messageSize_bytes
    o = overheadPerPacket_bytes
    m = maximumNPacketSize_bytes
    val = (s + (o * ((s + o) / m))) / m
    per_packet = s + (o * ((s + o) / m))
    return (val - math.floor(val)) * per_packet


# TESTS
ans = (10000 + (20 * 7)) / number_fragments(10000, 20, 1500) 
print(ans / 8)
print(number_fragments(10000, 20, 1500))
print (last_fragment_size(10000, 100, 1000))
