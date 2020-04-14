#!/usr/bin/env python3
from sys import argv
net_str=argv[1]
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
####Получаем сеть и маску из ввода,разделив строку по '/'
ip=net_str.split('/')[0].split('.')
mask=net_str.split('/')[1]
####Получаем бинарный вид маски из mask
mask_bin='1'*int(mask)+'0'*(32-int(mask))
####Получаем бинарный вид введенного адреса
ip_bin='{:08b}{:08b}{:08b}{:08b}'.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3]))
####Получаем адрес сети(в двоичном формате), обрезая ip_bin по маске и переводим его в список десятичных чисел
net_bin=ip_bin[0:int(mask)]+'0'*(32-int(mask))
net=[int(net_bin[0:8],2),int(net_bin[8:16],2),int(net_bin[16:24],2),int(net_bin[24:32],2)]
####Получаем список из бинарной маски(в десятичных значениях)
mask_l=[int(mask_bin[0:8],2),int(mask_bin[8:16],2),int(mask_bin[16:24],2),int(mask_bin[24:32],2)]
####Выводим
print(net_out_templ.format(net[0],net[1],net[2],net[3]))
print(mask_out_templ.format(mask_l[0],mask_l[1],mask_l[2],mask_l[3],mask))