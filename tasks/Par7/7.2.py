with open('Par7_files/config_sw1.txt','r') as file:
    for line in file:
        if line.startswith('!'):
            pass
        else:
            print(line.rstrip())