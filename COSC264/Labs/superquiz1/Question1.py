def composepacket (version, hdrlen, tosdscp, totallength, identification, flags, fragmentoffset, timetolive, protocoltype, headerchecksum, sourceaddress, destinationaddress):
    if version != 4:
        return 1
    elif hdrlen.bit_length() > 4 or hdrlen.bit_length() < 0:
        return 2
    elif tosdscp.bit_length() > 6 or tosdscp.bit_length() < 0:
        return 3
    elif totallength.bit_length() > 16 or totallength.bit_length() < 0:
        return 4
    elif identification.bit_length() > 16 or identification.bit_length() < 0:
        return 5
    elif flags.bit_length() > 3 or flags.bit_length() < 0:
        return 6
    elif fragmentoffset.bit_length() > 13 or fragmentoffset.bit_length() < 0:
        return 7
    elif timetolive.bit_length() > 8 or timetolive.bit_length() < 0:
        return 8
    elif protocoltype.bit_length() > 8 or protocoltype.bit_length() < 0:
        return 9
    elif headerchecksum.bit_length() > 16 or headerchecksum.bit_length() < 0:
        return 10
    elif sourceaddress.bit_length() > 32 or sourceaddress.bit_length() < 0:
        return 11
    elif destinationaddress.bit_length() > 32 or destinationaddress.bit_length() < 0:
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

    return out

print(composepacket(5,5,0,4000,24200,0,63,22,6,4711, 2190815565, 3232270145))
print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145))
