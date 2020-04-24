trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    '''
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/1':[10, 20, 30],
         'FastEthernet0/2':[11, 30],
         'FastEthernet0/4':[17]}
    trunk_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме trunk с конфигурацией на основе шаблона
    '''
    result={}
    for intf in intf_vlan_mapping.keys():
        a=result.setdefault(intf)
        result[intf]=[]
        for cmd in trunk_template:
            if 'allowed' in cmd:
                vlans_list=[]
                for vlan in intf_vlan_mapping[intf]:
                    vlans_list.append(str(vlan))
                result[intf].append(cmd+' '+','.join(vlans_list))
            else:
                result[intf].append(cmd)
    return(result)
print(generate_trunk_config(trunk_config,trunk_mode_template))