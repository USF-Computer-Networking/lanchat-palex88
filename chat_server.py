import socket

def run_server(UDP_IP_ADDRESS, UDP_PORT_NO):
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

    while True:
        data, addr = serverSock.recvfrom(6789)
        print "Message: ", data

if __name__ == '__main__':
    run_server("192.168.42.86", 6789)
