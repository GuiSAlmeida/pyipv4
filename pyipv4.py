import re


class PyIpv4:
    def __init__(self, ip, mask='255.255.255.0', cidr=24):
        self.ip = ip
        self.mask = mask
        self.cidr = cidr
        self._set_broadcast()
        self._set_network()

    @property
    def ip(self):
        return self._ip

    @property
    def mask(self):
        return self._mask

    @property
    def cidr(self):
        return self._cidr

    @property
    def network(self):
        return self._network

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def ips_num(self):
        return self._get_ip_num()

    @property
    def range(self):
        return self._get_range()

    @ip.setter
    def ip(self, ip):
        if not self._ip_validate(ip):
            raise ValueError('Invalid IP!')

        self._ip = ip
        self._ip_bin = self._ip_to_bin(ip)

    @mask.setter
    def mask(self, mask):
        if not mask:
            return
        if not self._ip_validate(mask):
            raise ValueError('Invalid Mask!')

        self._mask = mask
        self._mask_bin = self._ip_to_bin(mask)

        if not hasattr(self, 'cidr'):
            self.cidr = self._mask_bin.count('1')

    @cidr.setter
    def cidr(self, cidr):
        if not cidr:
            return

        if not isinstance(cidr, int):
            raise TypeError('CIDR needs a integer number.')

        if cidr > 32:
            raise ValueError('CIDR exceeds the limit of 32Bits.')

        self._cidr = cidr
        self._mask_bin = (cidr * '1').ljust(32, '0')

        if not hasattr(self, 'mask'):
            self.mask = self._bin_to_ip(self._mask_bin)

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

    @staticmethod
    def _bin_to_ip(ip):
        octets_len = 8
        blocs = [int(ip[i:octets_len + i], 2)
                 for i in range(0, 32, octets_len)]

        ip_decimal = [str(bloc) for bloc in blocs]
        return '.'.join(ip_decimal)

    def _set_broadcast(self):
        host_bits = 32 - self.cidr
        self._broadcast_bin = self._ip_bin[:self.cidr] + (host_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast

    def _set_network(self):
        host_bits = 32 - self.cidr
        self._network_bin = self._ip_bin[:self.cidr] + (host_bits * '0')
        self._network = self._bin_to_ip(self._network_bin)
        return self._network

    def _get_ip_num(self):
        return (2 ** (32 - self.cidr)) - 2

    def _get_range(self):
        host_bits = 31 - self.cidr
        self._first_host_bin = self._ip_bin[:self.cidr] + (host_bits * '0' + '1')
        self._last_host_bin = self._ip_bin[:self.cidr] + (host_bits * '1' + '0')
        self._first_host = self._bin_to_ip(self._first_host_bin)
        self._last_host = self._bin_to_ip(self._last_host_bin)
        return f'{self._first_host} - {self._last_host}'
