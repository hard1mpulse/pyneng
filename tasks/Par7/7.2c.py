from sys import argv
path_to_file='Par7_files/'+argv[1]
ignore = ['duplex', 'alias', 'Current configuration']
skip_line=False
result_file_name=argv[2]
result=open('Par7_files/'+result_file_name,'w')
with open(path_to_file,'r') as file:
    for line in file:
        for i in ignore:
            if i in line:
                skip_line=True
                break
            else:
                skip_line=False
        if skip_line:
            pass
        else:
            result.write(line)
result.close()