import matplotlib.pyplot as plt
import numpy as np

Fs = 150.0
Ts = 1.0/Fs
t = np.arange(0,1.,Ts)
d = [1., 1., 1., 0., 1., 1.]
ff = 5
s = []
z = []
tn = np.arange(0,len(d)*1.,Ts)

for x in d:
    if x==1:
        for y in t:
            z.append(1)
            k = np.sin(2 * np.pi * ff * y)
            s.append(k)
    else:
        for y in t:
            z.append(0)
            k = np.sin(2 * np.pi * ff * y + np.pi)
            s.append(k)

fig, ax = plt.subplots(2, 1)
ax[0].plot(tn,z)
ax[0].set_xlabel('Bit')
ax[0].set_ylabel('Tempo')
ax[1].plot(tn,s)
ax[1].set_xlabel('Freq')
ax[1].set_ylabel('Tempo')
plt.show()