<center>

# COSC264 Notes - Networking

</center>

> [TOC]

### General Info About Course

Note that although a number of assessments are closed-book, we will be permitted to bring an A4 hand written sheet of paper, this can be double sided but must be *hand written*.

#### Grading
- Lab quizzes (16%)
    - Four in first term (2% each)
    - Four in second term (2% each)
- Super quiz on packet processing (7%)
    - Open during week 3
- Socket programming assignment (10%)
    - Due: Sunday, August 16, 2020, 11:59pm
- Mid-term test (25%)
  - 90 minutes
  - Closed-book, mostly electronic
  - Covers all first term content
  - Friday September 11, 2020 7:00 - 8:00pm
- Lab test(17%)
    - 60 minutes
    - closed-book
    - Friday, October 9, 7:00pm
    - Held in Jack Erskine Labs (TBC)
    - Covers material from labs in second term
- Final exam (25%)
    - 90 minutes
    - closed-book
    - time and place to be determined

> In order to pass this course, you must meet the following criteria, an average of 50%
> across all assessments, and an average mark of at least 45% on invigilate assessments 
> (mid-term, lab test and final exam).

#### Resources
- [Lecture Notes](https://learn.canterbury.ac.nz/course/view.php?id=9047&section=1)
- [Problem Sheets](https://learn.canterbury.ac.nz/course/view.php?id=9047&section=2)
- Principles of Digital Transmission – With Wireless Applications
    - Sergio Benedetto and Ezio Biglieri
- Principles of Digital Communication
    -  Robert G. Gallager
- Data and Computer Communications
    - William Stallings
- Computer Networks.
    - Andrew S. Tanenbaum and David J. Wetherall

### Introduction to Networking

#### Terminology
| Term         | Description                                                                                                       |
| ------       | -----------                                                                                                       |
| End Stations | These are the items connecting to a user ie a computer, servers etc. these are always connected to other stations |
| Network      | A loose term used in many ways, but essentially is a path for information flow                                    |
| Router       | Connects networks together so data can flow from one network to another                                           |

#### First look at the internet

**Where do routers send traffic?** 
> Routers do not normally generate any traffic of their own, they are there to connect
> networks from point to point, they make routing decisions in order to indicate where
> to send the traffic to.

**How can I connect overseas then?**
> Parts of the internet are owned by service providers. These companies own large cables 
> that go overseas to allow companies to connect their networks to the world, service
> providers sell connectivity for a price, your local internet providers will purchase
> access from the largest providers, the top level service providers tend to provide to
> each other, however this tends to not be paid for as it is a mutual benefit for both
> companies to be more connected.

#### Delay - Quality of Service >> Write Types of delay
| Application                          | Data loss     | bandwidth                               | Delay-sensitive   |
| ---                                  | ---           | ---                                     | ---               |
| File Transfer                        | No loss       | Elastic                                 | No                |
| Email                                | No loss       | Elastic                                 | no                |
| Web pages                            | No loss       | Mostly elastic, minimum rate desireable | no                |
| Internet telephony videoconferencing | Loss-tolerant | Audio/Voice: few kbps                   | <= 200 - 250 ms   |
| Streaming audio/video                | Loss-tolerant | same as above                           | a few seconds     |
| interactive games                    | Loss-tolerant | few kbps - 1 mbps                       | few hundred ms    |
| instant messaging                    | No loss       | Elastic                                 | not very, depends |

> The term `elastic` means: these applications have no strict minimum-bandwidth requirements, they are just find with what they get

### Bitwise operations

**Bitwise `AND` Operation**

The `AND` operation works by multiplying each bit in the first string to the bits in the
second string, in the python interpreter, the symbol `~` denotes the bitwise `AND`. The 
following example will multiple two binary numbers.

```python
# Here is a python example of a bitwise AND operation
binary_first = 0b0110110110
binary_second = 0b1100011101

bitwise_first_AND_second = binary_first & binary_second
print(bitwise_first_AND_second)
```
> Result: 01 0001 0100

**Bitwise `OR` Operation**

The `OR` operation works by checking if the bit is equal to *1*, if it is equal to 1 then
put 1, else put 0.

```python
# This is how to preform the bitwise function manually
output = ""
if see == 1:
    output.append(1)
else:
    output.append(0)
print(reversed(output))
```

To actually preform this in python, you would use the `|` operand to denote the `OR` bitwise
function. The following is how to preform this in python.

```python
# Here is a python example of a bitwise OR operation
binary_first = 0b0110110110
binary_second = 0b1100011101

bitwise_first_OR_second = binary_first | binary_second
print(bitwise_first_OR_second)
```


### Communication Patterns

##### Unicast
- Only two nodes in the networks involved
- One is the transmitter, the other the receiver, but the nodes can have both roles
- Goal: reproduce exactly at the chosen reciever the bit stream sent by the transmitter
- Example
    - phone connections
    - viewing a web page

##### Broadcast
- One node as sender, all other as recievers
- Goal: reporiduce exactly at all stations in the network the bit stream is sent by the transmitter
- Example
    - Radio
    - TV

##### Multicast
- One node as sender, several but not all recievers
- Goal: reproduce exxactly at some stations in the network the bit stream is sent by the transmitter
- often, in multicast groups all nodes can act as senders
- Example
    - Internet chat
    - Phone confrence

#### Client Server Paradigm

The server allocates an address to each client connected. The client acts by sending requests and then turns off
when it receives its answer, the server will stay on and wait for requests to enter. Servers need to have powerful
programs for all users, this is why most servers are hosted on multiple machines that act as the same address to
connect on

One server has multiple clients, and the server has to provide a request `n` times for `n` users.

#### Peer-to-Peer Paradigm
- Has no centralised network
    - this means that it avoids a single point of failure

A peer to peer network is a two way street, you have to both provide data in order to benefit by getting your service.

> an example of this is torrents - you have to upload in order to gain the download

#### Circuit and Packet Switching

The design of a network is strongly influenced by the traffic it is supposed to carry, this will shape the netowrk.

##### Circuit Switching

**Voice Traffic**

- In today's POTS voice is transmitted digitally, the analog voice signal is A/D-converted with fixed sampling rates and resolution
    - Data rate: 64kbit/s
- The voice data is generated continously at a fixed rate
    - The provider has to be able to provide this rate continuously by the period or the voice quality will drop dramatically
- This is called a continuous bit rate (CBR) data stream
- No one else's connection is allowed to interfere with our own
- Goal: provide the illusion of having your own connection with the end user
    - this is achieved by the server allocating a certain amount of `bandwidth` to your call
    - at the end of the call, the resources are re-allocated to a new user 
- Other examples of CBR data: CBR Video, periodic sensor measurements

> When we are recording audio, we do not take the whole thing, we have a 256 bit storage, and we `sample` the data in order to store it.

**Properties of Circuit Switching**
- A routing descision is only made once
- A connection has its resources guaranteed
- Any bandwidth not used by a connection cannot be re-used by other connections
- Connection setup takes time, it does not pay off when only very little data needs to be transmitted
- Connection setup may fail when no route or insufficient resources are available in the network

##### Packet Switching
- Many data applications naturally have time-varying rates
- called `Variable-bit-rate (VBR)` or `bursty` traffic
- CS-networks are not well suited to VBR traffic

**Properties of Packet Switching**
- Data flows are segmented into packets
- Packets are basic unit of transmission
- Packets consist of:
    - A `packet header` containing meta-information about the packet
    - The `packet payload` 
    - Possibly a `packet trailer` for error detection
- Packets are transmitted individually
- There is no notion of a connection, packets can be sent immediately without having to setup any state or resource reservation
- Congestion *To many cars on the highway* can cause packet loss
    - we allocate *buffer memory* to back these packets, if we run out of memory, we must drop some of the incoming packets
- The internet is a Packet-Switching network
*Conequences*
- Lack of resourcse reservation means there are no guarantees for packet delivery
    - Internet/IP "best effort" service: packet is delivered/not delivered
    - IP's lack of guarantees is compensated in parts by TCP
    - **Routers in packet-switched networks perform more complex processing during information transfer than
switching fabrics in circuit-switched networks**
- Packet size
    - Packet overheads (header, trailer) have fixed size
    - Payload size is variable (within bounds)
    - Tradeoff
        - Small size payload leads to high overhead ratio
        - Small payload size leads to reduced susceptibility to errors
    - Packet size limits can be technology or application driven
        - to long packets might block important packets from being sent for an unacceptable time
- Router will not accept packet until it accepts the whole packet and sees trailer (due to corruption)

**Protocols and Services**
- Packets can get lost, re-ordered, delayed, modified or be tampered with
- Stations (end hosts or routers) can implement procedures to repair these problems
- These procedures run in a distributed fashion (as different stations need to cooperate) and are called **protocols**
- Protocols are rules and procedures underlying data transfer

We need to use sequence numbers in order to keep values in order online (such as if we had
a book, we need to make sure page one is ordered before page two, as if we purely rely on
page one arriving before page two, this will not work as we cannot guarantee that the packet
containing page one will not be lost). This is why we should send timers, and other things included
within the trailer of a packet.

The role of IP in the internet protocol Stack
- IP = Internet Protocol
- There are two protocol versions *4, 6* here we use *IPv4*
- Everything over IP, IP over everything

**IP Addresses**
- Each host is identified by one or more IP addresses
    - A host has many IP addresses as it has network adapters
    - End hosts usually have only one IP address (as we use the one with widest scope)
- The IP address not only identifies the host but also helps the network find the path to this host
- Humans normally do not work with IP directly but with host names such as www.canterbury.ac.nz
- There exists a special service/protocol called the domain name service (`DNS`) which translates to human-readable host names to IPv4 addresses, the internet itself only works
    with IPv4 addresses
- Suppost to be worldwide unique (not really true anymore)
- unacknowledged (post service does not send back feedback)
- no guaranteed order of packets recieved with IPv4 protocol

### Socket Programming
