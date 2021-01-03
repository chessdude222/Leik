from ODEsolver import *

class RK2(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        u1 = u[k] + dt/2*(f(u[k], t[k+1]) + f(u[k], t[k]))
        new = u[k] + dt/2*(f(u1, t[k+1]) + f(u[k], t[k]))
        return new

def f(u, t):
    return -u

time = np.linspace(0,3,31)
method = RK2(f)
method.set_initial_condition(1)
u, t = method.solve(time)

print(t, u)
