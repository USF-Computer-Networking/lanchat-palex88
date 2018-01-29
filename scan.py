import sys
import socket

from scapy.all import *


def get_host_name():
    return socket.gethostbyname(socket.gethostname())


def check_lan(ip_address):
    return scapy._version()


if __name__ == '__main__':

    ip_address = get_host_name()
    print ip_address
    print check_lan(ip_address)
