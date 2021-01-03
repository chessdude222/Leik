import numpy as np
import matplotlib.pyplot as plt
import sys

def midpoint(f, Y, N, dt):
    N = int(N)
    y = np.zeros(N + 1)
    t = np.zeros(N + 1)
    y[0] = Y
    y[1] = y[0] + dt*f(y[0], 0)
    t[1] = dt
    for k in range(1, N):
        y[k+1] = y[k-1] + 2*dt*f(y[k], t[k])
        t[k+1] = t[k] + dt
    return t, y

A, N, dt = [float(i) for i in sys.argv[1:]]
Y = 1

exact = lambda t: np.exp(-A*t)
f = lambda y,t: -A*y
t, y = midpoint(f, Y, N, dt)
print(t, y)
plt.plot(t, y, 'r', label = 'midpoint')
plt.plot(t, exact(t), 'b', label = 'exact')
plt.legend()
plt.show()
