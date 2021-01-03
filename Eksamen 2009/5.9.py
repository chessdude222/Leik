from ODEsolver import *
import numpy as np
import matplotlib.pyplot as plt

class Diff:
    def __init__(self, p, q, A, c, s):
        self.p = p
        self.q = q
        self.A = A
        self.c = c
        self.s = s

    def __call__(self, u, t):
        A, p, q, c = self.A, self.p, self.q, self.c
        u0, u1 = u
        u0_d = u1
        u1_d = A*np.sin(c*t) - p*abs(u1)*u1 - q*np.sin(u0)
        return [u0_d, u1_d]

f = Diff(0.1, 1, 1, 2, np.pi/2)
time = np.linspace(0, 30*np.pi, 451)
problem = RungeKutta4(f)
problem.set_initial_condition([f.s, 0])
u, t = problem.solve(time)
v = u[:,0]
plt.plot(t, v)
plt.show()
