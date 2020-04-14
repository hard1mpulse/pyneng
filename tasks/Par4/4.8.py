ip = '192.168.3.1'
ip_l=ip.split('.')
template = '''
    {0:<10} {1:<10} {2:<10} {3:<10}
    {0:010b} {1:010b} {2:010b} {3:010b}
    '''
print(template.format(int(ip_l[0]),int(ip_l[1]),int(ip_l[2]),int(ip_l[3])))