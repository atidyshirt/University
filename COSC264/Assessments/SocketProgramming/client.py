import socket

# These are the inputs
IP = socket.gethostbyname('localhost')
PORT = 1024
DATE = 'date' # or time

def checkInputs(DATE, IP, PORT):
    if not IP:
        return "The IP address is not specified"
    if PORT < 1024 and PORT > 64000:
        return "The Port number is not within specified range (1024, 64000)"
    if DATE != 'date' or DATE != 'time':
        return "Make sure the client asks for the date or time"


def format_request(Date):
    """
    Formats the packet into the desired format
    """
    MagicNo = 0x497E
    PacketType = 0x0001
    if Date == 'date':
        RequestType = 0x0001
    elif Date == 'time':
        RequestType = 0x0002
    bytelist = []
    bytelist.append(MagicNo.to_bytes(2, 'big'))
    bytelist.append(PacketType.to_bytes(2, 'big'))
    bytelist.append(RequestType.to_bytes(2, 'big'))
    arrayBytes = bytearray()
    for x in bytelist:
        arrayBytes += x
    return arrayBytes

request_packet = format_request(DATE)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # set to grab IPv4 and socket_stream is to create TCP protocols

#  s.settimeout(1)
s.connect((IP, PORT)) # This is the port number (1024)
s.sendto(request_packet, (IP, PORT))

# To terminate the client in a loop
complete_message = ""

while True:
    msg = s.recv(48) # this is just a message with the number of bytes alocated to each packet (if we lower this, we must use a loop to get all the data)

    if len(msg) <= 0:
        break

    complete_message += msg.decode("utf-8")

print(complete_message)
s.close()
