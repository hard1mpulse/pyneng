# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
route=[]

with open("ospf.txt","r") as file:
    for line in file:
        route=line.split()
        print(f"""
Prefix                {route[1]}
AD/Metric             {route[2].strip("[]")}
Next-Hop              {route[4].strip(",")}
Last update           {route[5].strip(",")}
Outbound Interface    {route[6]}
""")
