mac = 'AAAA:BBBB:CCCC'
mac = mac.replace(':','')
print('{:b}{:b}{:b}{:b}{:b}{:b}'.format(int(mac[0:2],16),int(mac[2:4],16),int(mac[4:6],16),int(mac[6:8],16),int(mac[8:10],16),int(mac[10:12],16)))