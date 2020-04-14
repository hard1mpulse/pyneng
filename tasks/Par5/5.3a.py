access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
access_template.append('Введите номер VLAN:')
trunk_template.append('Введите разрешенные VLANы:')
templates={'access': access_template, 'trunk': trunk_template }
portmode=input('Введите режим работы интерфейса (access/trunk): ')
intf=input('Введите тип и номер интерфейса: ')
question=templates[portmode].pop(-1)
vlans=input(question)
print('interface '+intf+'\n'+('\n').join(templates[portmode]).format(vlans))
