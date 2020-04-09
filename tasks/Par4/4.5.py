command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
vlans1=set(command1.split('vlan ')[1].split(','))           ###Получаем множество вланов из команды1
vlans2=set(command2.split('vlan ')[1].split(','))           ###Получаем множество вланов из команды2
vlans=list(vlans1.intersection(vlans2))                     ###Получаем список из пересечения двух множеств
print(sorted(vlans))

