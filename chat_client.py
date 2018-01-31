import  argparse
from socket import *

import scan

MY_IP = "192.168.42.86"
BROADCAST_IP = "255.255.255.255"
DEFAULT_PORT = 9999
MESSAGE = "Hello, Server"

def run():

    parser = argparse.ArgumentParser()
    parser.parse_args()

    ip_dict = scan.make_arp_dict()
    for k, v in ip_dict.iteritems():
        print "Hostname: " + v + " IP Address: " + k
    print "\n"

    addr = MY_IP
    port = DEFAULT_PORT

    input = raw_input("Enter IP address to broadcast to. If none, message will be broadcast.")
    if ip_dict.has_key(input):
        addr = input
    else:
        print "IP not in local network, set to broadcast.\n"

    port_alt = raw_input("Default port set to 9999. Enter a new port or hit enter to leave default.")
    if port_alt.isdigit() & len(port_alt) == 4:
        port = port_alt
    else:
        print "Not a valid port. Port is set to 9999.\n"

    print 'Type "quit" to exit chat.'


    while True:

        client_sock = socket(AF_INET, SOCK_DGRAM)
        client_sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

        mess = raw_input()
        if mess.lower() == "quit":
            return False
        else:
            client_sock.sendto(mess, (addr, port))


if __name__ == '__main__':
    run()
