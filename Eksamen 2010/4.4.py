import numpy as np
import matplotlib.pyplot as plt

def T(x,t):
    return np.exp(-q*x)*np.cos(t-q*x)

q = 1
x = np.linspace(0,3,31)
t = np.linspace(0, 6*np.pi, 97)

lines = plt.plot(x, T(x,t[0]))

for i in t:
    lines[0].set_ydata(T(x,i))
    plt.draw()
    plt.pause(0.01)
