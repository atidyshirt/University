def payload (pkt):
    headerlen = (pkt[0] & 0b00001111) * 4
    return pkt[headerlen:]

print(payload(bytearray(b'E\x00\x00\x17\x00\x00\x00\x00@\x06i\x8d\x11"3DUfw\x88\x10\x11\x12')))

