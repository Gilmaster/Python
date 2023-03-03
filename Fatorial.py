# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 11:11:54 2022

@author: Gilvan
"""

def fatorial(num): 
    if num < 0: 
        print("Fatorial de numero negativo não existe")

    elif num == 0: 
        return 1
        
    else: 
        f = 1
        while(num > 1): 
            f *= num 
            num -= 1
        return f 

num = float(input("informe o numero: ")); 

print("Fatorial de",num,"é", fatorial(num)) 

