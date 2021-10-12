from pyipv4 import PyIpv4

ip_address = input('Enter IP Address: ')
network_mask = input('Enter Mask: ')
cidr = int(input('CIDR Notation: '))

pyipv4 = PyIpv4(ip=ip_address, mask=network_mask, cidr=cidr)

print('-'*20+'Result'+'-'*20, end='\n\n')
print(f'IP Address: {pyipv4.ip}')
print(f'Network Address: {pyipv4.network}')
print(f'Number of Usable Hosts: {pyipv4.ips_num}')
print(f'Broadcast Address: {pyipv4.broadcast}')
print(f'Subnet Mask: {pyipv4.mask}')
print(f'CIDR Notation: {pyipv4.cidr}')
print(f'Usable Host IP Range: {pyipv4.range}')
