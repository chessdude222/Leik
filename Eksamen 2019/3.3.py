from ODEsolver import *

class Heun3(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        k1 = dt*f(u[k], t[k])
        k2 = dt*f(u[k] + k1/3, t[k] + dt/3)
        k3 = dt*f(u[k] + 2*k2/3, t[k] + 2*dt/3)
        return u[k] + k1/4 + 3*k3/4

rhs = lambda u,t: -0.5*u
solver = Heun3(rhs)
solver.set_initial_condition(1.0)
time = np.linspace(0,10,101)
u, t = solver.solve(time)

print(u,t)
