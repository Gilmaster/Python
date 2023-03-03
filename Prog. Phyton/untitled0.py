# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 19:23:00 2022

@author: Gilvan
"""
while True:
    nome = input("Nome: ")
    
    if len(nome) == 0:
        continue
    
    if (nome == '-1'):
        break
    
    n1 = float(input("Nota da primeira prova: "))
    n2 = float(input("Nota da segunda prova: "))

    media = (n1 + n2)/2

    if media > 7:
        print("O aluno %s foi aprovado com media %.2f" % (nome, media))
    else:
        print("O aluno %s foi reprovado com media %.2f" % (nome, media))

    nome = input("Nome: ")
    
print("Fim!")