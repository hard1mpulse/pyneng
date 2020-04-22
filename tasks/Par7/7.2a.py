from sys import argv
path_to_file='/home/python/Documents/task_templ/Par7_files/'+argv[1]
ignore = ['duplex', 'alias', 'Current configuration']
skip_line=False
with open(path_to_file,'r') as file:
    for line in file:
        for i in ignore:
            if i in line or line.startswith('!'):
                skip_line=True
                break
            else:
                skip_line=False
        if skip_line:
            pass
        else:
            print(line.rstrip())