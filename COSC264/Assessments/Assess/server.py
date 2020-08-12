import socket
import select
import datetime

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

def getDate():
    """
    grabs the current date using datetime, 
    and returns it as a string.
    """
    date = str(datetime.datetime.utcnow())
    date = date.split(" ")
    return date[0]

# Setting up server socket
host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # to reuse address and port 
host_socket.bind((IP, PORT))
host_socket.listen()

# able to keep track of sockets, making the host_socket index 0
sockets_list = [host_socket]

def receive_request(client_socket):
    """
    This function will grab the request from the client, and allow us to process it
    """
    try:
        request_header = client_socket.recv(HEADER_LENGTH)

        if not len(request_header):
            return False

        request_length = int(request_header.decode('utf-8').strip())

        return {'header': request_header, 'data': client_socket.recv(request_length)}

    except:
        return False

while True:
# This line will grab a subset of avalible sockets 
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for socket_in in read_sockets:
            if socket_in == host_socket:
                # for new sockets connecting, allow them to connect to host
                client_socket, client_address = host_socket.accept()
                sockets_list.append(client_socket)
            else:
                req = receive_request(socket_in)
                # if user requests the date by inputting date, send it the date
                if req == 'date':
                    message = getDate()


    sockets_list.append(client_socket)
