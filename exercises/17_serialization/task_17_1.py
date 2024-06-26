# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла,
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""

def write_dhcp_snooping_to_csv(filenames: list,output: str):
    import re,csv
    pattern=re.compile(r'(?P<mac>\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)\s+'
                        r'(?P<ip>\d+\.\d+\.\d+\.\d+)\s+'
                        r'(?:\d{1,5})\s{7}(?:dhcp-snooping)\s+'
                        r'(?P<vlan>\d+)\s+'
                        r'(?P<interface>\S+/\d{1,2})\n')
    dev_name_pattern=re.compile(r'^[^_]*')
    with open(output,'w',newline="") as result_file:
        writer= csv.DictWriter(result_file,fieldnames=['switch','mac','ip','vlan','interface'])
        writer.writeheader()
        for filename in filenames:
            result={}
            result.update({'switch':dev_name_pattern.match(filename).group()})
            with open(filename) as file:
                for bind in pattern.finditer(file.read()):
                    result.update(bind.groupdict())
                    writer.writerow(result)



if __name__ == "__main__":
    write_dhcp_snooping_to_csv(["sw1_dhcp_snooping.txt","sw2_dhcp_snooping.txt","sw3_dhcp_snooping.txt"],'test.txt')