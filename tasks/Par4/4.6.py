ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route=ospf_route.replace('O','OSPF')
route=ospf_route.split()
route.remove('via')
route[2]=route[2].strip('[]')
route[3]=route[3].strip(',')
route[4]=route[4].strip(',')
template='''
    Protocol:           {:15}
    Prefix:             {:15}
    AD/Metric:          {:15}
    Next-Hop:           {:15}
    Last update:        {:15}
    Outbound Interface: {:15}
    '''
print(template.format(route[0],route[1],route[2],route[3],route[4],route[5]))