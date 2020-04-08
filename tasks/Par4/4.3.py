config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
vlans=config.split('vlan ')[1].split(',')     ### Делим строчку по 'vlan ',далее то что справа делим по ','
print(vlans)