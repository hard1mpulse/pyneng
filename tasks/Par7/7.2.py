from sys import argv
path_to_file='Par7_files/'+argv[1]
with open(path_to_file,'r') as file:
    for line in file:
        if line.startswith('!'):
            pass
        else:
            print(line.rstrip())