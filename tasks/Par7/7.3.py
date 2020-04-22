with open('Par7_files/CAM_table.txt','r') as file:
    mac_table_begins=False
    mac_printed=False
    for line in file:
        if not mac_table_begins:
            pass
        else:
            mac_param=line.strip().split()
            print("{:6} {:17} {:7}".format(mac_param[0],mac_param[1],mac_param[3]))
            mac_printed=True
        mac_table_begins = True if '----    -----------       --------    -----'==line.strip() or mac_printed else False