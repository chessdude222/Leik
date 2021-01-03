from ODEsolver import *
import numpy as np
import matplotlib.pyplot as plt


class Diff:
    def __init__(self, m, L, c, g, theta):
        self.m = m
        self.L = L
        self.c = c
        self.g = g
        self.theta = theta

    def __call__(self, u, t):
        m, c, L, = self.m, self.c, self.L
        u0, u1 = u
        u0_d = u1
        u1_d = -1/(m*L)*(c*abs(u1)*u1 + m*g*np.sin(u0))
        return [u0_d, u1_d]

m = 1; L = 1; c = 1; g = 9.81; theta = 1
P = np.pi*2/np.sqrt(g)
# P/40*400 = 10P
time = np.linspace(0, 10*P, 401)

pendulum = Diff(m, L, c, g, theta)
problem = RungeKutta4(pendulum)
problem.set_initial_condition([pendulum.theta, 0])
u, t = problem.solve(time)
v = u[:,0]
plt.plot(t, v, 'b')
plt.show()
