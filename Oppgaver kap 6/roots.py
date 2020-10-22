import numpy as np
from math import pi
import matplotlib.pyplot as plt

def roots(r, theta, n):
    x_k = []
    y_k = []
    for k in range(n):
        x_k.append(r**(1.0/n)*np.cos((theta+2*pi*k)/n))
        y_k.append(r**(1.0/n)*np.sin((theta+2*pi*k)/n))
    return x_k, y_k

x_calculated1, y_calulated1 = roots(10**(-4), 2*pi, 6)
x_calculated2, y_calulated2 = roots(10**(-4), 2*pi, 12)
x_calculated3, y_calulated3 = roots(10**(-4), 2*pi, 24)

plt.plot(x_calculated1, y_calulated1, 'ro', Label='n=6')
plt.plot(x_calculated2, y_calulated2, 'go', Label='n=12')
plt.plot(x_calculated3, y_calulated3, 'bo', Label='n=24')
plt.legend()
plt.xlabel('real part')
plt.ylabel('imaginary part')
plt.show()
