import numpy as np
import matplotlib.pyplot as plt

def T(x,t):
    return np.exp(-q*x)*np.cos(t-q*x)

q = 1
x = np.linspace(0,3,31)
y = T(x,1)
plt.plot(x,y)
plt.show()
