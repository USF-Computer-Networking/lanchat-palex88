import sys
import socket
from subprocess import check_output

from scapy.all import *

import scanipaddress


def get_local_ip():
    return get_host_name

def get_host_name():
    return socket.gethostbyname(socket.gethostname())


def arp_network():
    return check_output(["arp", "-a"])


if __name__ == '__main__':

    print "Your IP address is " + get_host_name() + "\n"

    all_hosts = (arp_network())

    ip_objects = []
    for arp_addr in all_hosts.splitlines():
        ip_address = arp_addr.split(" ")[0]
        host_name = arp_addr.split(" ")[1]
        ip_objects.append(scanipaddress.ScanIpAddress(ip_address, host_name))

    for host in ip_objects:
        print host
