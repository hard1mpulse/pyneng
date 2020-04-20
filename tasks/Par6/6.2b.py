answered=False
while not answered:
    ip=input('Enter IP-address: ')
    ip_l=ip.split('.')
    correct=len(ip_l)==4
    if correct:
        for n in ip_l:
            if correct:
                try:
                    correct=int(n)>=0 and int(n)<=255
                except ValueError:
                    correct=False
            else:
                break
    if correct:
        if int(ip_l[0]) >= 1 and int(ip_l[0]) <= 223:
            print('\nunicast')
            answered=True
        elif int(ip_l[0]) >= 224 and int(ip_l[0]) <= 239:
            print('\nmulticast')
            answered=True
        elif ip=='255.255.255.255':
            print('\nlocal broadcast')
            answered=True
        elif ip=='0.0.0.0':
            print('\nunassigned')
            answered=True
        else:
            print('\nunused')
            answered=True
    else:
        print('IP-address incorrect!\n')