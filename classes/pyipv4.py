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
        if not self._ip_validate(ip):
            raise ValueError('Ip inválido!')
        self._ip = ip

    @mask.setter
    def mask(self, mask):
        if not mask:
            return
        if not self._ip_validate(mask):
            raise ValueError('Máscara inválida!')
        self._mask = mask
        self._mask_bin = self._ip_to_bin(mask)

    @cidr.setter
    def cidr(self, cidr):
        if not cidr:
            return

        if not isinstance(cidr, int):
            raise TypeError('Cidr precisa ser um número inteiro.')

        if cidr > 32:
            raise ValueError('Cidr excede limite de 32Bits.')

        self._cidr = cidr

    @staticmethod
    def _ip_validate(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}\.?){4}$'
        )
        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_to_bin(ip):
        blocs = ip.split('.')
        octets = [bin(int(bloc))[2:].zfill(8) for bloc in blocs]
        return ''.join(octets)
