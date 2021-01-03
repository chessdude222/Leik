from ODEsolver import *

class Heun3(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        k1 = dt*f(u[k], t[k])
        k2 = dt*f(u[k] + k1/3, t[k] + dt/3)
        k3 = dt*f(u[k] + 2*k2/3, t[k] + 2*dt/3)
        return u[k] + k1/4 + k3*3/4

f = lambda u, t: 2
"""
problem = Heun3(f)
problem.set_initial_condition(1)
u,t = problem.solve(np.linspace(0, 10, 101))
print(u,t)

def rhs(u,t):
    a = 1; R = 50
    return a * u*(1 - u/R)

# I assume the class is in the same file
time = np.linspace(0, 20, 201); U0 = 0.1
problem = Heun3(rhs)
problem.set_initial_condition(U0)
u, t = problem.solve(time)
print(u)
# u is the solution
"""
import matplotlib.pyplot as plt

def SEIS(S0, E0, p, q, r, T):
    # Defines the system of ODEs
    def f(u, t):
        S, E, I = u     # U is an vector with the values S(t), I(t) and E(t)
        s_d = -p(t)*S*I + r*I
        e_d = p(t)*S*I - q*E
        i_d = q*E - r*I
        return [s_d, e_d, i_d]
    time = np.linspace(0, T, 10*T + 1) # 10*T + 1 is the number of points
    # I assume the defined class is in the same file or imported
    problem = Heun3(f)
    problem.set_initial_condition([S0, E0, 0]) # I(0) = 0
    u, t = problem.solve(time)
    # u contains the solution, so we need to slice out the different values
    S, E, I = u[:,0], u[:,1], u[:,2]
    return S, E, I, t

S0 = 4.0; E0 = 0.2; q = 0.1; r= 0.1; p = lambda t: 0.0233; T = 100

S, E, I, t = SEIS(S0, E0, p, q, r, T)

plt.plot(t,S,t,E,t,I)
plt.legend(['S', 'E', 'I'])
plt.show()
