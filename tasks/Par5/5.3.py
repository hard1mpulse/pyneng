access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
templates={'access': ('\n').join(access_template), 'trunk': ('\n').join(trunk_template) }
portmode=input('Введите режим работы интерфейса (access/trunk): ')
intf=input('Введите тип и номер интерфейса: ')
vlans=input('Введите номер влан(ов): ')
print('interface '+intf+'\n'+templates[portmode].format(vlans))
