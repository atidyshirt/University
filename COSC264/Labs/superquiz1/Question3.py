def destaddress (pkt):
    # 17 - 20
    address = str(str(int(pkt[16])) + '.' + str(int(pkt[17])) + '.' + str(int(pkt[18])) + '.' + str(int(pkt[19])))
    a = (pkt[16] << 24) & 0b11111111000000000000000000000000
    b = (pkt[17] << 16) & 0b00000000111111110000000000000000
    c = (pkt[18] << 8) & 0b00000000000000001111111100000000
    d = (pkt[19] & 0b00000000000000000000000011111111)
    dest = a + b + c + d
    return (dest, address)


print(destaddress(bytearray(b'E\x00\x00\x1e\x04\xd2\x00\x00@\x06\x00\x00\x00\x124V3DUf')))
