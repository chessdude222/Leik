
import numpy as np
class ForwardEuler:
    """
    Class attributes:
    t: array of time values
    u: array of solution values (at time points t)
    k: step number of the most recently computed
    solution
    f: callable object implementing f(u, t)
    U0: initial condition (scalar or array)
    """
    def __init__(self, f, U0, T, n):
        if not callable(f):
            raise TypeError('f is not a function')
        self.f = lambda u, t: np.asarray(f(u, t))
        self.t = np.linspace(0,T,n+1)
        self.k = 0
        if isinstance(U0, (float,int)): # scalar ODE
            self.neq = 1
            self.u = np.zeros(n+1)
        else: # system of ODEs
            U0 = np.asarray(U0)
            self.neq = U0.size
            self.u = np.zeros((n+1,self.neq))
        self.U0 = U0

    def solve(self):
        """
        Solve the ODE from time 0 to T.
        Store solution in self.u.
        Return self.u and self.t.
        """
        u, t = self.u, self.t
        u[0] = self.U0

        for i in range(len(u)-1):
            self.k = i
            self.dt = t[i] - t[i-1]
            u[i+1] = self.advance()
        return self.t, self.u

    def advance(self):
        dt, u, f, k, t= self.dt, self.u, self.f, self.k, self.t
        return u[k] + dt*f(u[k], t[k])

def f(u, t):
    return u

solver = ForwardEuler(f, 1.0, 10, 100)
u, t = solver.solve()
print(u,t)
