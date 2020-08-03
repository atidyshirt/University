def revisedcompose (hdrlen, tosdscp, identification, flags, fragmentoffset, timetolive, protocoltype, sourceaddress, destinationaddress, payload):
    # Validity Checks
    version = 4
    if hdrlen.bit_length() > 4 or hdrlen.bit_length() < 0 or hdrlen < 5:
        return 2
    if tosdscp.bit_length() > 6 or tosdscp.bit_length() < 0:
        return 3
    if identification.bit_length() > 16 or identification.bit_length() < 0:
        return 5
    if flags.bit_length() > 3 or flags.bit_length() < 0:
        return 6
    if fragmentoffset.bit_length() > 13 or fragmentoffset.bit_length() < 0:
        return 7
    if timetolive.bit_length() > 8 or timetolive.bit_length() < 0:
        return 8
    if protocoltype.bit_length() > 8 or protocoltype.bit_length() < 0:
        return 9

    totallength = hdrlen
    for x in payload:
        totallength += x.bit_length()

    headerchecksum = 0

    # 16-bit ones 
    first = (version << 12) | (hdrlen << 8) | (tosdscp << 2)
    second = (totallength)
    third = (identification)
    fourth = (flags << 13) | fragmentoffset
    fifth = (timetolive << 8) | protocoltype
    sixth = headerchecksum

    #32 bit ones 
    seven = sourceaddress
    eight = destinationaddress

    X = first + second + third + fourth + fifth + sixth + seven + eight

    while X > 0xFFFF:
        x0 = X & 0xFFFF
        x1 = X >> 16
        X = x0 + x1

        X = ~X

        headerchecksum = (X << 16) & 0xFFFF

    if headerchecksum.bit_length() > 16 or headerchecksum.bit_length() < 0:
        return 10
    if sourceaddress.bit_length() > 32 or sourceaddress.bit_length() < 0:
        return 11
    if destinationaddress.bit_length() > 32 or destinationaddress.bit_length() < 0:
        return 12

    #FIRST 32
    version = version << 28
    hdrlen = hdrlen << 24
    tosdscp = tosdscp << 16
    #totallength 

    #SECOND 32
    identification = identification << 16
    flags = flags << 13
    #fragoff

    #THIRD 32
    timetolive = timetolive << 24
    protocoltype = protocoltype << 16
    #headerchecksum

    #FOURTH 32
    #source address
    #destination address

    first = version | hdrlen | tosdscp | totallength
    second = identification | hdrlen | fragmentoffset
    third = timetolive | protocoltype | headerchecksum
    fourth = sourceaddress
    fifth = destinationaddress

    bytelist = []

    bytelist.append(first.to_bytes(4, 'big'))
    bytelist.append(second.to_bytes(4, 'big'))
    bytelist.append(third.to_bytes(4, 'big'))
    bytelist.append(fourth.to_bytes(4, 'big'))
    bytelist.append(fifth.to_bytes(4, 'big'))

    out = bytearray()

    for byte in bytelist:
        out += byte

    out += payload

    return out

print(revisedcompose (6, 24, 4711, 0, 22, 64, 0x06, 0x22334455, 0x66778899, bytearray([0x10, 0x11, 0x12, 0x13, 0x14, 0x15])))
