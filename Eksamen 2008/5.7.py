from ODEsolver import *
import matplotlib.pyplot as plt

class Midpoint(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        if k == 0:
            return u[k] + dt*f(u[k], 0)
        else:
            return u[k - 1] + 2*dt*f(u[k], t[k])

A = 1
time = np.linspace(0, 5, 51)
exact = lambda t: np.exp(-A*t)
f = lambda y,t: -A*y

problem = Midpoint(f)
problem.set_initial_condition(1)
u, t = problem.solve(time)

plt.plot(t, u, label = 'midpoint')
plt.plot(t, exact(t), label = 'exact')
plt.legend()
plt.show()
