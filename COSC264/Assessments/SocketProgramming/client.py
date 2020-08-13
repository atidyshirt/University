import socket
import argparse

def start_client(DATE, HOST, PORT):
# These are the inputs
    IP = socket.gethostbyname(HOST)

    def checkInputs(DATE, IP, PORT):
        if not IP:
            print("The IP address is not specified")
            return False
        if PORT < 1024 or PORT > 64000:
            print("The Port number is not within specified range (1024:64000)")
            return False
        if DATE != 'date' and DATE != 'time':
            print("MSG parameter must be set to `date` or `time`")
            return False
        return True

    def decrypt_message(packet):
        info = [packet[i:i+1] for i in range(0, len(packet), 1)]
        if len(info) < 13:
            print("Packet does not include minimum headersize")
            return -1

        MagicNo = int.from_bytes(info[0] + info[1], 'big')
        
        if MagicNo != 0x497E:
            print("MagicNo is incorrect: `{}` recieved, must equal `0x497E`".format(MagicNo))
            return -1
        PacketType = int.from_bytes(info[2] + info[3], 'big')
        if PacketType != 0x0002:
            print("PacketType is incorrect: `{}` received, must equal `0x0002`".format(PacketType))
        LanguageCode = int.from_bytes(info[4] + info[5], 'big')
        if LanguageCode < 0x0001 or LanguageCode > 0x0003:
            print("LanguageCode is incorrect: `{}` received, must be within range (1, 3)".format(LanguageCode))
            return -1
        Year = int.from_bytes(info[6] + info[7], 'big')
        if Year > 2100:
            print("Year is incorrect: `{}` received, must be below 2100".format(Year))
            return -1
        Month = int.from_bytes(info[8], 'big')
        if Month < 1 or Month > 12:
            print("Month is incorrect: `{}` received, must be between 1 and 12".format(Month))
            return -1
        Day = int.from_bytes(info[9], 'big')
        if Day < 1 or Day > 31:
            print("Day is incorrect: `{}` received, must be between 1 and 31".format(Day))
            return -1
        Hour = int.from_bytes(info[10], 'big')
        if Hour < 0 or Hour > 23:
            print("Hour is incorrect: `{}` received, must be within range (0, 23)".format(Hour))
            return -1
        Minute = int.from_bytes(info[11], 'big')
        if Minute < 0 or Minute > 59:
            print("Minute is incorrect: `{}` received, must be within range (0, 59)".format(Minute))
            return -1
        Length = int.from_bytes(info[12], 'big')
        text = bytearray()
        for i in range(13, len(info)):
            text += info[i]
        text = text.decode('utf-8')

        if len(info) != 13 + Length:
            print("Length of packet does not match packet received")
            return -1

        return text

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
        else:
            return -1
        bytelist = []
        bytelist.append(MagicNo.to_bytes(2, 'big'))
        bytelist.append(PacketType.to_bytes(2, 'big'))
        bytelist.append(RequestType.to_bytes(2, 'big'))
        arrayBytes = bytearray()
        for x in bytelist:
            arrayBytes += x
        return arrayBytes

    if checkInputs(DATE, IP, PORT):
        request_packet = format_request(DATE)
        if request_packet == -1:
            print("The `date` parameter must be set to either `date` or `time`")

        else:

                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # set to grab IPv4 and socket_stream is to create TCP protocols
                s.settimeout(1)
                s.sendto(request_packet, (IP, PORT))

                complete_message = bytearray()

                while True:
                    #  read, write, exception = select.select(sockets, [], [])

                    try:
                        msg, source = s.recvfrom(1024)

                        if len(msg) <= 0:
                            break

                        complete_message += msg

                    except socket.timeout:
                        print("Client socket timeout")
                        break

                    except socket.error:
                        print("Client socket timeout")
                        break

                    result = decrypt_message(complete_message)
                    if result != -1:
                        print(result)
                        break
                    s.close()


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("MSG", help="The message to receive from server must be `date` or `time`", type=str)
    parser.add_argument("HOST", help="The Hostname to connect to", type=str)
    parser.add_argument("PORT", help="The Port number to connect to", type=int)

    args = parser.parse_args()
    start_client(args.MSG, args.HOST, args.PORT)

if __name__ == "__main__":
    Main()



