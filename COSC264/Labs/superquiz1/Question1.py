def composepacket (version, hdrlen, tosdscp, totallength, identification, flags, fragmentoffset, timetolive, protocoltype, headerchecksum, sourceaddress, destinationaddress):
    if version != 4:
        return 1
    elif hdrlen.bit_length() > 4:
        return 2
    elif tosdscp.bit_length() > 6:
        return 3
    elif totallength.bit_length() > 16:
        return 4
    elif identification.bit_length() > 16:
        return 5
    elif flags.bit_length() > 3:
        return 6
    elif fragmentoffset.bit_length() > 13:
        return 7
    elif timetolive.bit_length() > 8:
        return 8
    elif protocoltype.bit_length() > 8:
        return 9
    elif headerchecksum.bit_length() > 16:
        return 10
    elif sourceaddress.bit_length() > 32:
        return 11
    elif destinationaddress.bit_length() > 32:
        return 12
    else:
        arguments = [version, hdrlen, tosdscp, totallength, identification, flags, fragmentoffset, timetolive, protocoltype, headerchecksum, sourceaddress, destinationaddress]
        bytelist = []
        for arg in arguments:
            if arg < 0:
                return -1

        bytelist.append(version.to_bytes(1, 'big'))
        bytelist.append(hdrlen.to_bytes(1, 'big'))
        bytelist.append(tosdscp.to_bytes(1, 'big'))
        bytelist.append(totallength.to_bytes(2, 'big'))
        bytelist.append(identification.to_bytes(2, 'big'))
        bytelist.append(flags.to_bytes(1, 'big'))
        bytelist.append(fragmentoffset.to_bytes(2, 'big'))
        bytelist.append(timetolive.to_bytes(1, 'big'))
        bytelist.append(protocoltype.to_bytes(1, 'big'))
        bytelist.append(headerchecksum.to_bytes(2, 'big'))
        bytelist.append(sourceaddress.to_bytes(4, 'big'))
        bytelist.append(destinationaddress.to_bytes(4, 'big'))

        out = bytearray()

        for byte in bytelist:
            out += byte

        return out

print(composepacket(5,5,0,4000,24200,0,63,22,6,4711, 2190815565, 3232270145))
print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145))
