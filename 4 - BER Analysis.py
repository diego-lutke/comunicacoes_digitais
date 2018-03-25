import numpy as np
import matplotlib.pyplot as plt

snr = np.arange(0,10,1)
ber1 = []
ber2 = []

for b in snr:
    lin = 10.0**(b/10.0)
    x = np.random.randint(2, size=5000000)
    bpsk1 = 2*x - 1
    std = 1.0/np.sqrt(2*lin)
    y1 = bpsk1 + std*np.random.randn(len(x))
    rx1 = (y1 >= 0)
    erro1 = (rx1 != x).sum()
    ber1.append(float(erro1)/float(len(x)))
    x_rand = np.concatenate((x, x), axis=0)
    bpsk2 = 2 * x_rand - 1
    y2 = bpsk2 + std*np.random.randn(len(x_rand))
    y2rec = (y2[0:len(x_rand)/2] + y2[len(x_rand)/2:len(x_rand)])/2.
    rx2 = (y2rec >= 0)
    erro2 = (rx2 != x).sum()
    ber2.append(float(erro2) / float(len(x)))

plt.plot(snr,ber1)
plt.yscale('log')
plt.xscale('linear')
plt.plot(snr,ber2)
plt.yscale('log')
plt.xscale('linear')
plt.show()