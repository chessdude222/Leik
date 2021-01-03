from ODEsolver import *
import matplotlib.pyplot as plt

class F:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def __call__(self, u, t):
        b, c = self.b, self.c
        u0, u1 = u
        u0_d = u1
        u1_d = -b*abs(u1)*u1 - c*np.sin(u0)
        return [u0_d, u1_d]

f = F(1, 0.2, 1)
time = np.linspace(0, 8*np.pi, 321)
problem = RungeKutta4(f)
problem.set_initial_condition([f.a, 0])
u,t = problem.solve(time)   
y = u[:,0]

plt.plot(t, y)
plt.show()
