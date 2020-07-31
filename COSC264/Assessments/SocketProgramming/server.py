import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # set to grab IPv4 and socket_stream is to create TCP protocols
s.bind((socket.gethostname(), 1026))
s.listen(1024)

while True: # while there is a connection
    clt, adr=s.accept() # As we established above, accept returns the connection and address (these are being assigned to variables)
    print(f"Connection to {adr} established")
    clt.send(bytes("Socket programming in python", "utf-8"))
    clt.close()
