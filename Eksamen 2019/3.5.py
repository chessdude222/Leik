import numpy as np
from ODEsolver import *
import matplotlib.pyplot as plt

def SEIS(S0, E0, p, q, r, T):
    def f(u,t):
        S, E, I = u
        s_d = -p(t)*S*I + r*I
        e_d = p(t)*S*I - q*E
        i_d = q*E - r*I
        return [s_d, e_d, i_d]
    time = np.linspace(0, T, int(T*10) + 1)
    problem = ForwardEuler(f)
    problem.set_initial_condition([S0, E0, 0])
    u,t = problem.solve(time)
    S, E, I = u[:,0], u[:,1], u[:,2]
    return S, E, I, t

S0 = 4; E0 = 0.2; q = 1; r = 1; p = lambda t: 0.0233; T = 100

S, E, I, t = SEIS(S0, E0, p, q, r, T)

plt.plot(t, S, t, E, t, I)
plt.legend(['Suspectible', 'Cannot infect others', 'Infected'])
plt.show()
