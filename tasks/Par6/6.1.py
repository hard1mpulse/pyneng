mac=['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco=[]
for m in mac:
    mac_c=m.replace(':','.')
    mac_cisco.append(mac_c)