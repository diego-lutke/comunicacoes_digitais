#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random as rd
import itertools as it
import matplotlib.pyplot as plt
import math as mt
from bitstring import BitArray

n = raw_input("Em qual ordem você deseja seu PSK? Lembre-se que a ordem de um PSK de qualquer ordem é igual a 2^n.\n")
n = int(mt.log(float(n),2))
check2 = False
while (check2 <> True):
    r = raw_input("Você deseja digitá-los? (s/n)\n")
    if r == 's':
        check1 = False
        while (check1 <> True):
            d = raw_input("Digite os dados que você deseja:\n Ex. 00 00 01 11 00 01 11 11\n")
            d = d.replace(" ", "")

            if len(d) % n == 0:
                check1 = True
            else:
                print('Faltou um dígito em sua entrada. Faça novamente!')
                check1 = False

        dlist = []
        w = 0
        while (w <> len(d)):
            dlist.append(d[w:w + n])
            w = w + n
        print(dlist)
        check2 = True
        conj = len(dlist)
    elif r == 'n':
        k = raw_input("Criarei os dados para você, mas para isso, me diga a quantidade de conjuntos de dados que serão enviados:\n")
        conj = int(k)*n
        dlist = []
        while conj <> 0:
            aur = rd.randrange(2)
            dlist.append(aur)
            conj = conj - 1
        check2 = True
    else:
        print('Sua resposta não foi compreendida. Tente novamente!')
        check2 = False

Fs = 150.0
Ts = 1.0/Fs
t = np.arange(0,1.,Ts)
ff = 5

s = []
z = []
tn = np.arange(0,len(dlist)/n,Ts)
dlist = [dlist[x:x+n] for x in xrange(0, len(dlist), n)]

nfases = 2**n
fases = (2.*np.pi)/nfases

fasesl = []
k = 0
while k < nfases:
    fasesl.append(fases*k)
    k = k + 1

compar = list(it.product([0, 1], repeat=n))
comparjoin = list(it.chain.from_iterable(compar))

k = n
for pp in fasesl:
    comparjoin.insert(k,pp)
    k = k + n + 1

comparjoin = np.asarray(comparjoin,dtype=np.float64)
comparjoin = comparjoin.reshape(nfases,(n+1))

dlist = np.asarray(dlist,dtype=np.float64)

print(comparjoin)
print(dlist)

for pp in dlist:
    for kk in comparjoin:
        juncao1 = "".join(str(pp[0:n]))
        juncao2 = "".join(str(kk[0:n]))
        if juncao1 == juncao2:
            for y in t:
                c = BitArray(pp)
                z.append(c.uint)
                k = np.cos(2 * np.pi * ff * y + kk[n])
                s.append(k)

fig, ax = plt.subplots(2, 1)
ax[0].plot(tn,z)
ax[0].set_xlabel('Tempo')
ax[0].set_ylabel('Bit')
ax[1].plot(tn,s,'r')
ax[1].set_xlabel('Tempo')
ax[1].set_ylabel('Amplitude')
plt.show()

