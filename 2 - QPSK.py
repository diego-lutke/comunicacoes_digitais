#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

check2 = False
while(check2 <> True):
    check1 = False
    while(check1 <> True):
        d = raw_input("Digite os dados que você deseja:\n Ex. 00 00 01 11 00 01 11 11\n")
        d = d.replace(" ", "")

        if len(d) % 2 == 0:
            check1 = True
        else:
            print('Faltou um dígito em sua entrada. Faça novamente!')
            check1 = False

    dlist = []
    n = 0
    while(n <> len(d)):
        dlist.append(d[n:n+2])
        n = n + 2

    verif = len(dlist) - 1

    while(verif <> 0):
        if dlist[verif] == '00' or dlist[verif] == '01' or dlist[verif] == '11' or dlist[verif] == '10':
            check2 = True
            verif = verif - 1
        else:
            check2 = False
            verif = 0
            print('Você digitou um número acima de 11, tente novamente!')

Fs = 150.0
Ts = 1.0/Fs
t = np.arange(0,1.,Ts)
ff = 5

s = []
z = []
tn = np.arange(0,len(dlist)*1.,Ts)

for x in dlist:
    if x=='00':
        for y in t:
            z.append(0)
            n = 0.
            k = np.cos(2 * np.pi * ff * y + n*((np.pi) / 2.))
            s.append(k)
    elif x=='01':
        for y in t:
            z.append(1)
            n = 1.
            k = np.cos(2 * np.pi * ff * y + n*((np.pi) / 2.))
            s.append(k)
    elif x=='10':
        for y in t:
            z.append(2)
            n = 2.
            k = np.cos(2 * np.pi * ff * y + n*((np.pi) / 2.))
            s.append(k)
    elif x=='11':
        for y in t:
            z.append(3)
            n = 3
            k = np.cos(2 * np.pi * ff * y + n*((np.pi) / 2.))
            s.append(k)

fig, ax = plt.subplots(2, 1)
ax[0].plot(tn,z)
ax[0].set_xlabel('Tempo')
ax[0].set_ylabel('Bit')
ax[1].plot(tn,s)
ax[1].set_xlabel('Tempo')
ax[1].set_ylabel('Amplitude')
plt.show()