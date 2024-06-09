# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

d_temp={}
d_temp.update({'trunk': "\n".join(trunk_template),'access':"\n".join(access_template)})

out_temp={"access": 'Введите номер VLAN:',"trunk": 'Введите разрешенные VLANы:' }

porttype=input(f"Введите режим работы интерфейса ({','.join(list(d_temp.keys()))}): ")
intname=input("Введите тип и номер интерфейса: ")
vlans=input(out_temp.get(porttype,'Такого типа порта нет!'))
print(f"interface {intname}")
print(d_temp.get(porttype,'Такого типа порта нет!').format(vlans))