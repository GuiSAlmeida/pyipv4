import re


class PyIpv4:
    def __init__(self, ip, mask=None, cidr=None):
        self.ip = ip
        self.mask = mask
        self.cidr = cidr

    @property
    def ip(self):
        return self._ip

    @property
    def mask(self):
        return self._mask

    @property
    def cidr(self):
        return self._cidr

    @ip.setter
    def ip(self, ip):
        self._ip_validate(ip)
        self._ip = ip

    @mask.setter
    def mask(self, mask):
        self._mask = mask

    @cidr.setter
    def cidr(self, cidr):
        self._cidr = cidr

    @staticmethod
    def _ip_validate(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}\.?){4}$'
        )

        print(regexp.search(ip))
