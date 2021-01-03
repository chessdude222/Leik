import numpy as np
import matplotlib.pyplot as plt
from ODEsolver import *

class RK2(ODESolver):
    def advance (self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        k1 = dt*f(u[k], t[k])
        k2 = dt*f(u[k] + k1/2, t[k] + dt/2)
        return u[k] + k2

def flu(S0, I0, b, q, d, p, T):
    time = np.linspace(0, T, 5*T + 1)
    ini = [S0, I0, 0, 0]
    def f(u,t):
        S, I, R, V = u
        s_d = -b(t)*S*I - p(t)*S + d*R
        i_d = b(t)*S*I - q*I
        r_d = q*I - d*R
        v_d = p(t)*S
        return [s_d, i_d, r_d, v_d]

    problem = RK2(f)
    problem.set_initial_condition(ini)
    u, t = problem.solve(time)
    S, I, R, V = u[:,0], u[:,1], u[:,2], u[:,3]
    return t, S, I, R, V

S0 = 1000; I0 = 2; q = 1/7; b = lambda t: 0.001; d = 1/100; T = 40
def p(t):
    return np.where(t < 5, 0, 0.4)

t, S, I, R, V = flu(S0, I0, b, q, d, p, T)

plt.plot(t,S,t,I,t,R,t,V)
plt.legend(['Suspectible', 'Infected', 'Recovered', 'Vaccinated'])
plt.show()
