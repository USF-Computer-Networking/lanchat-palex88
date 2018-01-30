import sys
import socket
from subprocess import check_output

from scapy.all import *

import scanipaddress


def get_host_name():
    return socket.gethostbyname(socket.gethostname())


def arp_network():
    return check_output(["arp", "-a"])


def create_ip_addresses():
    return


if __name__ == '__main__':

    local_ip_address = get_host_name()
    test = (arp_network())

    ip_objects = []
    for arp_addr in test.splitlines():
        ip_address = arp_addr.split(" ")[0]
        host_name = arp_addr.split(" ")[1]
        ip_objects.append(scanipaddress.ScanIpAddress(ip_address, host_name))

    print len(ip_objects)
