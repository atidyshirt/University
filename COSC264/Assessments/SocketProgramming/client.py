import socket

HEADERSIZE = 5
IP = socket.gethostbyname('localhost')
PORT = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # set to grab IPv4 and socket_stream is to create TCP protocols
s.connect((IP, PORT)) # This is the port number (1024)

# To terminate the client in a loop
complete_message = ""

new_msg = True
while True:
    msg = s.recv(48) # this is just a message with the number of bytes alocated to each packet (if we lower this, we must use a loop to get all the data)

    if len(msg) <= 0:
        break

    if new_msg:
        msglen = int(msg[:HEADERSIZE])
        new_msg = False

    complete_message += msg.decode("utf-8")

    if len(complete_message) - HEADERSIZE == msglen:
        print(complete_message[HEADERSIZE:])
        new_msg = True
        full_message = ""

print(complete_message)
