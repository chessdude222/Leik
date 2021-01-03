from oppgave33 import Heun
import matplotlib.pyplot as plt
import numpy as np

def predator_prey(x0, y0, r, a, m, b, T, n):
    def f(u, t):
        x, y = u
        return r*x - a*x*y, -m*y + b*x*y

    U0 = [x0, y0]
    solver = Heun(f, U0, T, n)
    t, u = solver.solve()
    x_array = u[:,0]
    y_array = u[:,1]
    return t, x_array, y_array

r = 1; m = 1; a = 0.3; b = 0.2; x0 = 1; y0 = 1; T = 20; n=100

t, x, y = predator_prey(x0, y0, r, a, m, b, T, n)
plt.plot(t, x, label = 'x')
plt.plot(t, y, label = 'y')
plt.show()
