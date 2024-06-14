# -*- coding: utf-8 -*-
"""
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать
на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов,
а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
"""
def generate_description_from_cdp(filename: str):
    import re
    pattern=re.compile(r"^(?P<remote_device>\S+)\s+(?P<local_intf>\S+ \S+)\s+(?:\d+).*(?P<remote_intf>\S{3} \S+)$")
    descr_template="description Connected to {} port {}"
    result={}
    with open(filename) as file:
        for line in file:
            if pattern.search(line):
                print("Match found!")
                match=pattern.match(line)
                result.update({match.group('local_intf'): descr_template.format(match.group("remote_device"),match.group("remote_intf"))})
    return result
