ip=input('Enter IP-address: ')
if int(ip.split('.')[0]) >= 1 and int(ip.split('.')[0]) <= 223:
    print('\nunicast')
elif int(ip.split('.')[0]) >= 224 and int(ip.split('.')[0]) <= 239:
    print('\nmulticast')
elif ip=='255.255.255.255':
    print('\nlocal broadcast')
elif ip=='0.0.0.0':
    print('\nunassigned')
else:
    print('\nunused')