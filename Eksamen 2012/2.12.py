from ODEsolver import *

class ForwardEuler(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        new = u[k] + (t[k+1] - t[k])*f(u[k], t[k])
        return new
