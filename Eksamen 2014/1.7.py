from ODEsolver import *
import numpy as np


class RK2(ODESolver):
    def advance (self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        k1 = dt*f(u[k], t[k])
        k2 = dt*f(u[k] + k1/2, t[k] + dt/2)
        return u[k] + k2

def test_RK2():
    f = lambda u,t: 2 + (u - (2*t + 3))**2
    time = np.linspace(0, 10, 11)
    expected = 2*time + 3
    problem = RK2(f)
    problem.set_initial_condition(3)
    u, t = problem.solve(time)
    for com, expected in zip(u, expected):
        assert com == expected

test_RK2()
