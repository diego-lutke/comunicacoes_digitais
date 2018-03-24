#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import math as mt

'''Fs = 150.0
Ts = 1.0/Fs
t = np.arange(0,1.,Ts)

r = raw_input("Você deseja digitar os dados que serão transmitidos? (s/n)\n")
if r == 's':
    d = raw_input("Digite os dados que você deseja:\n Ex. 00 00 01 11 00 01 11 11\n")
    d = d.replace(" ", "")
    dlist = []
    n = 0
    while (n <> len(d)):
        dlist.append(d[n:n + 2])
        n = n + 2
elif r == 'n':
    k = raw_input("Criarei os dados para você, mas para isso, me diga a quantidade de bits que você deseja enviar:\n")
    conj = int(k)
    dlist = []
    aur = []
    while conj <> 0:
        aur = np.random.randint(2)
        dlist.append(aur)
        conj = conj - 1
    print(dlist)

ff = 5
s = []
z = []
tn = np.arange(0,len(dlist)*1.,Ts)

for x in dlist:
    if x==1:
        for y in t:
            z.append(1)
            k = np.sin(2 * np.pi * ff * y)
            s.append(k)
    else:
        for y in t:
            z.append(0)
            k = np.sin(2 * np.pi * ff * y + np.pi)
            s.append(k)'''

EboverNo = [0., 1., 2., 3., 4., 5., 6., 7., 8., 8., 10.]
ber = []

for b in EboverNo:
    lin = 10.0**(b/10.0)
    x = np.random.randint(2,size=5000000)
    bpsk = 2*x - 1
    std = 1.0/np.sqrt(2*lin)
    y = bpsk + std*np.random.randn(len(x))
    rx = (y >= 0)
    erro = (rx != x).sum()
    ber.append(float(erro)/float(len(x)))

'''x = n.pr
x_red npconcatenate([x,y],axis=)

y1 = ylab'b]
y2 = y[b*1.fim]'''

print(ber)

'''fig1, ax = plt.subplots(2, 1)
ax[0].plot(tn,z)
ax[0].set_xlabel('Bit')
ax[0].set_ylabel('Tempo')
ax[1].plot(tn,s)
ax[1].set_xlabel('Freq')
ax[1].set_ylabel('Tempo')
plt.show()'''

plt.plot(EboverNo,ber)
plt.yscale('log')
plt.xscale('linear')
plt.show()