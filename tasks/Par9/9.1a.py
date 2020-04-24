access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}
port_security_template = [
    'switchport port-security maximum 2',
    'switchport port-security violation restrict',
    'switchport port-security'
    ]

def generate_access_config(intf_vlan_mapping, access_template,psecurity=None):
    '''
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    '''
    result=[]
    for intf in intf_vlan_mapping.keys():
        result.append(intf)
        for cmd in access_template:
            if 'vlan' in cmd:
                result.append(cmd+' '+str(intf_vlan_mapping[intf]))
            else:
                result.append(cmd)
        if psecurity!=None:
            for cmd in psecurity:
                result.append(cmd)
        else:
            pass


    return(result)
print(generate_access_config(access_config,access_mode_template))
print(80*'-')
print(generate_access_config(access_config,access_mode_template,port_security_template))