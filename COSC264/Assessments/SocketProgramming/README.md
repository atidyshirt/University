# Socket Programming Assessment

> [TOC]

### Problem Description

Your task is to write two programs in Python.  The first one, called server will allow the other program, called client, to ask the server for the current date or time of day.  The server offers to deliver these in three different languages.



### Notes on Socket Programming in python

Sockets are endpoints built for sending and receive data 

#### How to use sockets in python

The first thing we need to do is to import the socket module using the python syntax `import socket`.

| Methods            | Description                                                                               |
| ---                | ---                                                                                       |
| `socket.socket()`  | used to create sockets (required on both server as well as client ends to create sockets) |
| `socket.accept()`  | used to accept a connection, returns a pair of values (conn, address)                     |
| `socket.bind()`    | Used to bind to the address that is specified as a parameter                              |
| `socket.close()`   | Used to bind to the address that is specified as a parameter                              |
| `socket.connect()` | Used to mark the socket as closed                                                         |
| `socket.listen()`  | used to connect to a remote address specified as the parameter                            |

#### What are Servers?

Servers are either a computer, program or device devoted to managing network resources and can be on the same device or local or remote

#### What are Clients?

Clients are computer or software that receives information or services. Clients request for services from the servers, the best example
is the Web Browser..

```python
# This is the server 

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # set to grab IPv4 and socket_stream is to create TCP protocols
s.bind((socket.gethostname(), 1024))
s.listen(5)

while True: # while there is a connection
    clt, adr=s.accept() # As we established above, accept returns the connection and address (these are being assigned to variables)
    print(f"Connection to {adr} established")
    clt.send(bytes("Socket programming in python", "utf-8"))
```

```python
# This is the client

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # set to grab IPv4 and socket_stream is to create TCP protocols
s.connect(socket.gethostname(), 1024) # This is the port number (1024)

msg = s.recv(1024) # this is just a message number

print(msg.decode("utf-8"))
```
