# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 19:16:08 2022

@author: Gilvan
"""

import math

frutas = ["banana","maçã","laranja","mamão"]
novas = ["pera", "abacaxi"]

for f in frutas:
    print(f)
    
#lista_frutas = frutas + novas
frutas += novas

print(frutas)