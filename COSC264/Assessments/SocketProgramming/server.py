import socket
import select
import datetime

HEADERSIZE = 5
IP = socket.gethostbyname('localhost')
PORT = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # set to grab IPv4 and socket_stream is to create TCP protocols

# This will allow us to reuse the same port number instead of having to bump up
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((IP, PORT))
s.listen(48)

# SERVERSIDE FUNCTIONS
def getDate():
    """
    grabs the current date using datetime, 
    and returns it as a string.
    """
    date = str(datetime.datetime.utcnow())
    date = date.split(" ")
    return date[0]

while True: # while there is a connection
    clt, adr=s.accept() # As we established above, accept returns the connection and address (these are being assigned to variables)
    print(f"Connection to {adr} established")
    msg = getDate()
    msg = f'{len(msg):<{HEADERSIZE}}' + msg 

    clt.send(bytes(msg, "utf-8"))
