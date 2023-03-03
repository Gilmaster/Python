# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 11:22:54 2022

@author: Gilvan
"""

n = int(input("Verificar numeros primos ate: "))
mult=0

for count in range(2,n):
    if (n % count == 0):
        mult += 1

if(mult==0):
    print(n, "é um numero primo")
else:
    print(n, "não um numero primo")