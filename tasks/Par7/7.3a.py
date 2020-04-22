with open('Par7_files/CAM_table.txt','r') as file:
    mac_table_begins=False
    mac_found=False
    mac_list=[]
    vlan_list=[]
    for line in file:
        if not mac_table_begins:
            pass
        else:
            mac_param=line.strip().split()
            mac_list.append(mac_param)
            if not (int(mac_param[0]) in vlan_list):
                vlan_list.append(int(mac_param[0]))
            mac_found=True
        mac_table_begins = True if '----    -----------       --------    -----'==line.strip() or mac_found else False
    vlan_list.sort()
    for vlan in vlan_list:
        for mac in mac_list:
            if int(mac[0])==vlan:
                print("{:6} {:17} {:7}".format(mac[0],mac[1],mac[3]))
            else:
                pass
