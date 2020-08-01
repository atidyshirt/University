def destaddress (pkt):
    # 17 - 20
    address = str(str(int(pkt[16])) + '.' + str(int(pkt[17])) + '.' + str(int(pkt[18])) + '.' + str(int(pkt[19])))
    dest = str(str(pkt[16]) + "" + str(pkt[17]) + "" + str(pkt[18]) + "" + str(pkt[19]))
    return (dest, address)


print(d staddress(bytearray(b'E\x00\x00\x1e\x04\xd2\x00\x00@\x06\x00\x00\x00\x124V3DUf')))
