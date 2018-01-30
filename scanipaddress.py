class ScanIpAddress:

    def __init__(self, host_name, ip_address):
        self.ip_address = ip_address
        self.host_name = host_name

    def __set__(self, instance, host_name):
        if self.host_name == "?":
            self.host_name = "Host name unavailable"

    @property
    def get_ip_address(self):
        return self.ip_address

    @property
    def get_host_name(self):
        return self.host_name

    def __str__(self):
        return self.host_name + " - " + self.ip_address
