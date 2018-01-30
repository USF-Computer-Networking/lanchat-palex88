import sys
import argparse
from socket import *
from select import select

UDP_IP_ADDRESS = "192.168.42.86"
UDP_PORT_NO = 6789
MESSAGE = "Hello, Server"

def run():

    parser = argparse.ArgumentParser
    parser.add_argument("-h", "--help", help="Get more info", required=False, default="")
    parser.add_argument("-p", type=int, help="Port to broadcast to. Default is 6789.", required=False, default=6789)
    parser.add_argument("-a", type=str, help="IP address to broadcast to. Default is multicast.", required=False, default="255.255.255.255")

    print 'Type "quit" to exit chat.'

    while True:

        client_sock = socket(AF_INET, SOCK_DGRAM)

        mess = raw_input()
        if mess.lower() == "quit":
            return False
        else:
            client_sock.sendto(mess, (addr, port))

        # sender = socket(AF_INET, SOCK_DGRAM)
        # receiver = socket(AF_INET, SOCK_DGRAM)
        # receiver.bind((addr, port))
        # sender.sendto(mess, (addr, port))
        #
        # while True:
        #     inputready, outputready, exceptready = select(input, [], [])
        #
        #     for s in inputready:
        #         if s in inputready:
        #             data, addr = receiver.recvfrom(port)
        #             print data
        #         elif s == sys.stdin:
        #             sender.sendto(sys.stdin.readline(), (addr, port))

if __name__ == '__main__':
    run()
