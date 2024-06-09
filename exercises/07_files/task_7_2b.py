# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv

with open(argv[1]) as file:
    result=open(argv[2],"w")
    for line in file:
        skipline=False
        for word in ignore:
            if word in line:
                skipline=True
                break
        if line.startswith("!"):
            continue
        elif skipline:
            continue
        else:
            result.write(line)
result.close()