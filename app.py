from classes.pyipv4 import PyIpv4

pyipv4 = PyIpv4(ip='192.168.0.1', mask='255.255.255.0', cidr=24)

print(f'IP: {pyipv4.ip}')
print(f'Máscara: {pyipv4.mask}')
print(f'Rede: {pyipv4.network}')
print(f'Broadcast: {pyipv4.broadcast}')
print(f'CIDR: {pyipv4.cidr}')
print(f'Número de ips: {pyipv4.ips_num}')

