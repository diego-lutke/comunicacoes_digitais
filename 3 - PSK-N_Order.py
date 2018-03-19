#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import random as rd

n = raw_input("Quantos símbolos você deseja?\n")
check2 = False
while (check2 <> True):
    r = raw_input("Você deseja digitá-los? (s/n)\n")
    if r == 's':
        check1 = False
        while (check1 <> True):
            d = raw_input("Digite os dados que você deseja:\n Ex. 00 00 01 11 00 01 11 11\n")
            d = d.replace(" ", "")

            if len(d) % int(n) == 0:
                check1 = True
            else:
                print('Faltou um dígito em sua entrada. Faça novamente!')
                check1 = False

        dlist = []
        w = 0
        while (w <> len(d)):
            dlist.append(d[w:w + int(n)])
            w = w + int(n)
        print(dlist)
        check2 = True
    elif r == 'n':
        k = raw_input("Criarei os dados para você, mas para isso, me diga a quantidade de conjuntos de dados que serão enviados:\n")
        conj = int(k)*int(n)
        dlist = []
        while conj <> 0:
            aur = rd.randrange(2)
            dlist.append(aur)
            conj = conj - 1
        check2 = True
    else:
        print('Sua resposta não foi compreendida. Tente novamente!')
        check2 = False