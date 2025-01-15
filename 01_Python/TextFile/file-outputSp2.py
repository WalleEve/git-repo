# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 09:51:38 2019

@author: Migration
"""

f = open ('Laptop.txt','w')
f.write('Name   processor    ram   price  \n')

f.write('....   .........    ...   .....  \n' )
f.write('Dell   i3 8th Gen    4    25000  \n' )
f.write('Lenovo i3 8th Gen    4    24000  \n' )
f.write('Hp     i3 7th Gen    4    28000  \n' )
f.write('Acer   i3 8th Gen    4    22000  \n' )

f.close

r = open('Laptop.txt','r')
message = r.read()
print (message)
r.close()

