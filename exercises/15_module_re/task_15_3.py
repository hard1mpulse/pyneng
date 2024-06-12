# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""

def convert_ios_nat_to_asa(ios_nat_file: str,asa_nat_file: str):
    import re
    asa_nat_template="""object network LOCAL_{ip}
 host {ip}
 nat (inside,outside) {method} interface service {protocol} {sport} {dport}
"""
    pattern=re.compile(r'\w+ \w+ \S+ \S+ (?P<method>\S+) (?P<protocol>\S+) (?P<ip>\S+) (?P<sport>\S+) \w+ \S+ (?P<dport>\S+)')
    with open(asa_nat_file,'w') as result_file:
        with open(ios_nat_file,'r') as input_file:
            f=input_file.read()
            for match in pattern.finditer(f):
                result_file.write(asa_nat_template.format(ip=match.group('ip'),protocol=match.group('protocol'),method=match.group('method'),
                                                          sport=match.group('sport'),dport=match.group('dport')))


convert_ios_nat_to_asa('cisco_nat_config.txt','asa_nat_config.txt')


