import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    x = x**2 - y**2
    y = 2*x*y
    return x, y

f_v = np.vectorize(f)

x_v = np.linspace(-2,2, 15)
y_v = np.linspace(-2,2, 15)
degrees = np.linspace(-2, 2, 30)

for a in degrees:
    line = lambda x: x*a
    x, y = f(x_v, line(x_v))
    plt.plot(x, y)

plt.show()
