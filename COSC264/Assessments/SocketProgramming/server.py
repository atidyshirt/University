import socket
import select
import datetime

header = 0
IP = socket.gethostbyname('localhost')
PORT_english = 1024
PORT_maori = 1025
PORT_german = 1026

s_english = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # set to grab IPv4 and socket_stream is to create TCP protocols
s_maori = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # set to grab IPv4 and socket_stream is to create TCP protocols
s_german = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # set to grab IPv4 and socket_stream is to create TCP protocols

server_sockets = [[s_english, PORT_english], [s_maori, PORT_maori], [s_german, PORT_german]]

# This will allow us to reuse the same port number instead of having to bump up
for sock, port in server_sockets:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((IP, port))
    sock.listen(48)

# SERVERSIDE FUNCTIONS
def packetCheck(packet):
    """
    checks the integrity of the packet, and makes sure that it is formatted correctly
    """
    print(packet)
    MagicNo = packet[:2]
    PacketType = packet[2:4]
    RequestType = packet[:-2]
    if MagicNo != 0x497E:
        return False
    if PacketType != 0x0001:
        return False
    if RequestType != 0x0001 or RequestType != 0x0002:
        return False
    return True

def getDate():
    """
    grabs the current date using datetime and returns it as a string.
    """
    date = str(datetime.datetime.utcnow())
    date = date.split(" ")
    return date[0]

while True: # while there is a connection
    for s, port in server_sockets:
        clt, adr=s.accept() # As we established above, accept returns the connection and address (these are being assigned to variables)
        print(f"Connection to {adr} established")
        packet, source = clt.recvfrom(48)
        print(f"{packetCheck(packet)}")
        if packetCheck(packet):
            msg = getDate()
            clt.send(bytes(msg, "utf-8"))
            clt.close()
        else:
            msg = "Packet is not correct"
            clt.send(bytes(msg, "utf-8"))
            clt.close()
