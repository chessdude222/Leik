import numpy as np
import matplotlib.pyplot as plt

ev = 1.6*10**(-19)
k = 8.6*10**(-5)
my = 4.74*1.6*10**(-19)

def f(E,T=0.1):
    return 1/(1+np.exp((E-my)/(k*T)))

E = np.linspace(0, 10*ev, 50)
f = f(E)

plt.plot(E,f, 'go')
plt.show()
