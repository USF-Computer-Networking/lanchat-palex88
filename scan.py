import socket


def get_host_name():
    return socket.gethostbyname(socket.gethostname())


def check_lan():
    return


if __name__ == '__main__':
    print(get_host_name())
