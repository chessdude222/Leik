import matplotlib.pyplot as plt
import numpy as np

class Diff:
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

    def diff1(self, x):
        h, f = self.h, self.f
        return (f(x+h) - f(x))/h

    def diff2(self, x):
        h, f = self.h, self.f
        return (f(x+h)-f(x-h))/(2*h)

    def diff3(self, x):
        h, f = self.h, self.f
        return (-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)

plt.figure(figsize=(10,10))
f = lambda x: np.sin(2*np.pi*x)
dfdx = lambda x: 2*np.pi*np.cos(2*np.pi*x)
x = np.linspace(-1, 1, 100)
y = dfdx(x)
plt.plot(x, y, 'p', label = 'exact')
h = [0.9, 0.6, 0.3, 0.1]

for i in h:
    a = Diff(f, i)
    plt.plot(x, a.diff1(x), 'g', label = f'diff1 h={i}')
    plt.plot(x, a.diff2(x), 'r', label = f'diff3 h={i}')
    plt.plot(x, a.diff3(x), 'm', label = f'diff3 h={i}')


plt.legend()
plt.show()
