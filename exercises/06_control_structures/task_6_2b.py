# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_correct=False
while not ip_correct:
    ip_address = input("введите ip-адрес: ")
    ip_correct=True

    for oct in ip_address.split('.'):
        if '.' not in ip_address:
            print('Неправильный IP-адрес')
            ip_correct=False
            break
        if len(ip_address.split('.')) != 4:
            print('Неправильный IP-адрес')
            ip_correct = False
            break
        try:
            o=int(oct)
        except ValueError:
            print('Неправильный IP-адрес')
            ip_correct=False
            break
        if o > 255 or o < 0:
            print('Неправильный IP-адрес')
            ip_correct=False
            break

    if ip_correct:
        oct1 = int(ip_address.split(".")[0])

        if ip_address == "255.255.255.255":
            print("local broadcast")
        elif ip_address == "0.0.0.0":
            print("unassigned")
        elif 1 <= oct1 <= 223:
            print("unicast")
        elif 224 <= oct1 <= 239:
            print("multicast")
        else:
            print("unused")