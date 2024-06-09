# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
def convert_ranges_to_ip_list(range_list: list):
    import ipaddress
    result=[]
    for ip_range in range_list:
        if "-" not in ip_range:
            result.append(ip_range)
        elif "-" in ip_range.split(".")[-1]:
            first_ip=ipaddress.ip_address(ip_range.split("-")[0])
            last_ip_list=ip_range.split(".")
            last_ip_list.pop(-1)
            last_ip=ipaddress.ip_address('.'.join(last_ip_list)+"."+ip_range.split("-")[-1])
            ip=first_ip
            while ip <= last_ip:
                result.append(str(ip))
                ip=ip+1
        else:
            first_ip=ipaddress.ip_address(ip_range.split("-")[0])
            last_ip=ipaddress.ip_address(ip_range.split("-")[1])
            ip=first_ip
            while ip <= last_ip:
                result.append(str(ip))
                ip = ip + 1
    return result

