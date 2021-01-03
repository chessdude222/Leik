from ODEsolver import *
import matplotlib.pyplot as plt
import numpy as np

class F:
    def __init__(self, m, L, c, g, theta):
        self.m = m
        self.L = L
        self.c = c
        self.g = g
        self.theta = theta

    def __call__(self, u, t):
        m, L, c, g = self.m, self.L, self.c, self.g
        u0, u1 = u
        u1_d = -1/(m*L)*(c*abs(u1)*u1 + m*g*np.sin(u0))
        return [u1, u1_d]

m = 1; L = 1; c = 1; g = 9.81; theta = 1
f = F(m, L, c, g, theta)
P = np.pi*2/np.sqrt(g)
time = np.linspace(0, 10*P, 401)
problem = RungeKutta4(f)
problem.set_initial_condition([f.theta, 0])
u, t = problem.solve(time)
v = u[:,0]

plt.plot(t, v, 'b')
plt.xlabel('t')
plt.ylabel('v')
plt.show()
