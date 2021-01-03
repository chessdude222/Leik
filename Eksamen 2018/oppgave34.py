# S(0) = S0, E(0) = E0, I(0) = 0, R(0) = 0
import numpy as np
import matplotlib.pyplot as plt
from ODEsolver import ForwardEuler

def SEIR(S0, E0, p, q, r ,T):
    time = np.linspace(0, T, 10*T + 1)
    def f(u, t):
        S, E, I, R = u
        s_d = -p(t)*S*I
        e_d = p(t)*S*I - q*E
        i_d = q*E - r*I
        r_d = r*I
        return [s_d, e_d, i_d, r_d]
    inital = [S0, E0, 0, 0]
    problem = ForwardEuler(f)
    problem.set_initial_condition(inital)
    u, t = problem.solve(time)
    return t, u[:,0], u[:,1], u[:,2], u[:,3]

S0 = 4; E0 = 0.2; q = 1; r = 0.1; T = 100
p = lambda t: 0.0233
t, S, E, I, R = SEIR(S0, E0, p, q, r, T)
plt.plot(t, S, label = 'S')
plt.plot(t, E, label = 'E')
plt.plot(t, I, label = 'I')
plt.plot(t, R, label = 'R')
plt.legend()
plt.show()
