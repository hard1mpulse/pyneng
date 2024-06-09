# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

output="{:4}     {:14}      {:4}"
vlan=input("Enter VLAN number: ")
with open("CAM_table.txt","r") as file:
    for line in file:
        if "DYNAMIC" in line:
            cam=line.split()
            if vlan == cam[0]:
                print(output.format(cam[0],cam[1],cam[3]))