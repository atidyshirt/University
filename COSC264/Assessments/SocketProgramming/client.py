import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # set to grab IPv4 and socket_stream is to create TCP protocols
s.connect((socket.gethostname(), 1026)) # This is the port number (1024)

# To terminate the client in a loop
complete_message = ""

while True:
    msg = s.recv(1024) # this is just a message with the number of bytes alocated to each packet (if we lower this, we must use a loop to get all the data)

    if len(msg) <= 0:
        break

    complete_message += msg.decode("utf-8")

print(complete_message)
