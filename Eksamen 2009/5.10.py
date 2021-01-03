d:
from ODEsolver import *

class Midpoint(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        if k == 0:
            return u[k] + dt*f(u[k], t[k])
        else:
            return u[k-1] + 2*dt*f(u[k], t[k])
