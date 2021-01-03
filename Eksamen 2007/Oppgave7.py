import sys
import matplotlib.pyplot as plt
import numpy as np

Y = float(sys.argv[1])
beta = float(sys.argv[2])
U = float(sys.argv[3])
g = 9.81

def f(x):
    return Y - 1/(2*U**2)*g*x**2/np.cos(beta)**2 + x*np.tan(beta)

c = Y
b = np.tan(beta)
a = -g/(np.cos(beta)**2*2*U**2)

x_1 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)

if x_1 > 0:
    x_g = x_1
elif x2 > 0:
    x_g = x2

print(x_1, x2)

time = np.linspace(0, x_g, int(x_g*50))
plt.plot(time, f(time))
plt.show()
