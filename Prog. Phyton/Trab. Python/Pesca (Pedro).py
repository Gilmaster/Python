# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 10:34:52 2022

@author: Gilvan
"""

p = float(input("Informe o peso em Kg pescado: "))

e = p-50

if e > 0:
    m = e*4
    print("A sua pesca excede o limite permitido nescessario pagamento adicinal de: R$","%.2f" %m)
    
else:
    print("Sua pesca esta dentro do limete permitido.")