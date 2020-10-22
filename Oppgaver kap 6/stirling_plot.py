import numpy as np
import matplotlib.pyplot as plt
import scipy.special

def exact(x):
    return np.log(scipy.special.gamma(x))

def stirling(x):
    return x*np.log(x) - x

values = np.linspace(1, 100, 100)

x_aprox = stirling(values)
x_exact = exact(values)

plt.plot(values, x_aprox, 'g', Label = 'approximate')
plt.plot(values, x_exact, 'r', label = 'exact')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
# plt.show()

x = 2
while (exact(x) - stirling(x))/exact(x) > 0.1:
    x += 1

print(x)
