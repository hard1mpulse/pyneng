# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename: str):
    with open(config_filename) as file:
        trunk_intfs={}
        access_infs={}
        for line in file:
            if "interface" in line:
                intf_name=line.split()[-1]
            elif "allowed vlan" in line:
                vlans = []
                for vlan in line.split()[-1].split(','):
                    vlans.append(int(vlan))
                trunk_intfs.update({intf_name: vlans})
            elif "mode access" in line:
                access_infs.update({intf_name: 1})
            elif "access vlan" in line:
                access_infs.update({intf_name: int(line.split()[-1])})
    return (access_infs,trunk_intfs,)

print(get_int_vlan_map('config_sw2.txt'))