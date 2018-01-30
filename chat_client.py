import socket

def run():
    UDP_IP_ADDRESS = "192.168.42.86"
    UDP_PORT_NO = 6789
    Message = "Hello, Server"

    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))


if __name__ == '__main__':
    run()
