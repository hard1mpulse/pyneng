def get_int_vlan_map(filename):
    '''
    filename - строка с именем файла конфига
    Возвращает два словаря(для trunk и access),которые содержат ключи с названиями интерфейсов и влан
    В случае access влан это число
    В случае trunk это список чисел
    '''
    access_map={}
    trunk_map={}
    with open('Par9_files/'+filename,'r') as f:
        intf_found=False
        intf_type=''
        is_intf_trunk=False
        for line in f:
            if 'interface FastEthernet' in line:
                intf_found=True
                intf=line.split()[-1]
            elif '!' in line:
                intf_found=False
            elif intf_found and 'switchport mode access' in line:
                is_intf_trunk=False
                a=access_map.setdefault(intf)
                access_map[intf]=1
            elif intf_found and 'trunk encapsulation dot1q' in line:
                is_intf_trunk=True
                a=trunk_map.setdefault(intf)
            else:
                pass
            if intf_found and not is_intf_trunk and 'switchport access vlan' in line:
                access_map[intf]=int(line.split()[-1])
            elif intf_found and is_intf_trunk and 'switchport trunk allowed vlan' in line:
                trunk_map[intf]=[]
                vlan_list=line.split()[-1].split(',')
                for vlan in vlan_list:
                    trunk_map[intf].append(int(vlan))
            else:
                pass
    return(access_map,trunk_map)
file=input('Enter cfg file name: ')
access_vlan_map,trunk_vlan_map=get_int_vlan_map(file)
print(access_vlan_map)
print('\n')
print('-'*80+'\n')
print(trunk_vlan_map)