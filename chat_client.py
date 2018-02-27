#!/usr/bin/env python

# File:           main.py
# Author:         Alex Thompson
# Github:         palex88
# Date Created:   2018-01-31
# Date Modified:  2018-02-26
# Python Version: 2.7

import argparse
from socket import *

import scan

MY_IP = "192.168.42.86"
BROADCAST_IP = "255.255.255.255"
DEFAULT_PORT = 9999
MESSAGE = "Hello, Server"


def run():

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="the port you want to use", type=int)
    parser.add_argument("-i", "--ip", help="the ip address you want to use", type=str)
    args = parser.parse_args()

    ip_dict = scan.make_arp_dict()
    for k, v in ip_dict.iteritems():
        print "Hostname: " + v + " IP Address: " + k
    print "\n"

    if args.ip:
        addr = args.ip
    else:
        addr = BROADCAST_IP

    if args.port:
        port = args.port
    else:
        port = DEFAULT_PORT

    ip_input = raw_input("Enter IP address to message. If none, message will be broadcast or sent to command line arg.")
    if ip_dict.has_key(ip_input):
        addr = ip_input
    else:
        print "IP not in local network, set to broadcast.\n"

    port_alt = raw_input("Default port set to 9999 or command line arg. "
                         "Enter a new port or hit enter to leave default.")
    if port_alt.isdigit() & len(port_alt) == 4:
        port = port_alt
    else:
        print "Not a valid port. Port is set to 9999.\n"

    print 'Type "quit" to exit chat.'

    client_sock = socket(AF_INET, SOCK_DGRAM)
    client_sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    # client_sock.bind((addr, port))

    while True:

        if client_sock.recvfrom(port) != None:
            data, addr = client_sock.recvfrom(port)
            print "Message: ", data
        else:
            mess = raw_input()
            if mess.lower() == "quit":
                return False
            else:
                client_sock.sendto(mess, (addr, port))


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        print '\nExiting'
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
