import numpy as np
import matplotlib.pyplot as plt

def N(t, k=0.2, B=50000, C=9):
    return B/(1+C*np.exp(-k*t))

t = np.linspace(0, 48, 49)
y = N(t)

plt.plot(t, y)
plt.show()
