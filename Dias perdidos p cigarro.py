# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 10:49:05 2022

@author: Gilvan
"""

c = int(input("informe a quantidade de cigarros consumidos: "))

m = c*10

h = m/60

d = h/24

if m < 60:
    print("seu tempo de vida perdido foi: ","%.2f" %m, "min")
    
elif h < 60:
    print("seu tempo de vida perdido foi: ","%.2f" %h, "horas")
    
else:
    print("seu tempo de vida perdido foi: ","%.2f" %d, "dias")