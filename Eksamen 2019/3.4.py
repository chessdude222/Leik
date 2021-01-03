from ODEsolver import *

class Heun3(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        k1 = dt*f(u[k], t[k])
        k2 = dt*f(u[k] + k1/3, t[k] + dt/3)
        k3 = dt*f(u[k] + 2*k2/3, t[k] + 2*dt/3)
        return u[k] + k1/4 + 3*k3/4

def rhs(u,t):
    a = 1; R = 50
    return a*u*(1 - u/R)

U0 = 0.1
time = np.linspace(0, 20, 201)
problem = Heun3(rhs)
problem.set_initial_condition(U0)
u,t = problem.solve(time)

print(u,t)
