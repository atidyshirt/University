def IPToString(addr):
    addr = addr.to_bytes(4, "big")
    return (
        str(int(addr[0]))
        + "."
        + str(int(addr[1]))
        + "."
        + str(int(addr[2]))
        + "."
        + str(int(addr[3]))
    )


print(IPToString(0x20304050))
