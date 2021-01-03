from ODEsolver import *

class Midpoint(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        k1 = dt*f(u[k], t[k])
        k2 = dt*f(u[k] + k1/2, t[k] + dt/2)
        u_new = u[k] + k2
        return u_new

def test_Midpoint():
    exact = lambda t: 5*t + 1
    deriv = lambda u,t: 5
    time = np.linspace(0, 10, 101)
    u0 = 1
    problem = Midpoint(deriv)
    problem.set_initial_condition(u0)
    u,t = problem.solve(time)
    calculated = exact(time)
    tol = 1E-12
    for u, c in zip(u, calculated):
        assert abs(u - c) < tol

test_Midpoint()
