# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 19:48:34 2022

@author: Gilvan
"""
i = 1
p = float(input("Quantidade do Produto: "))
v = int(input("Valor do produto: " ))
s = 0

while i <= p:
    s += v
    i += 1

print("Valor a pagar: R$", s)
    

    