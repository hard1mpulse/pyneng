# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""
import pprint


def parse_sh_ip_int_br(filename: str):
    import re
    import pprint
    result=[]
    pattern=re.compile(r'(\S+)\s+(\d+.\d+.\d+.\d+|unassigned) +\S+ +\S+ +(\bup\b|\badministratively down\b|\bdown\b) +(\bup\b|\badministratively down\b|\bdown\b)')
    with open(filename) as file:
        f=file.read()
        result=[intf_config for intf_config  in re.findall(pattern,f)]
        # for intf_config in :
    return result

pprint.pprint(parse_sh_ip_int_br('sh_ip_int_br.txt'))