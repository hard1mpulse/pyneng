net_str=input('Введите IP-сеть: ')
####Создаем темплейты вывода
net_out_templ='''
    Network:
    {0:<8} {1:<8} {2:<8} {3:<8}
    {0:08b} {1:08b} {2:08b} {3:08b}
    '''
mask_out_templ='''
    Mask:
    /{4}
    {0:<8} {1:<8} {2:<8} {3:<8}
    {0:08b} {1:08b} {2:08b} {3:08b}
    '''
####Получаем сеть и маску из ввода,разделив по '/'
net=net_str.split('/')[0]
mask=net_str.split('/')[1]
####Получаем бинарный вид маски из mask
mask_bin='1'*int(mask)+'0'*(32-int(mask))
print(mask_bin)
####Получаем список из бинарной маски(в десятичных значениях)
mask_l=[int(mask_bin[0:8],2),int(mask_bin[8:16],2),int(mask_bin[16:24],2),int(mask_bin[24:32],2)]
####Выводим
print(net_out_templ.format(int(net.split('.')[0]),int(net.split('.')[1]),int(net.split('.')[2]),int(net.split('.')[3])))
print(mask_out_templ.format(mask_l[0],mask_l[1],mask_l[2],mask_l[3],mask))