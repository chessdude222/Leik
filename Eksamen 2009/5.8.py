from ODEsolver import *
import numpy as np
import matplotlib.pyplot as plt

def f(h,t):
    return -(R/r)**(-2)*((1 + (r/R)**4))**(-0.5)*np.sqrt(2*g*h)


r = 1; R = 30; g = 9.81; h0 = 50; time = np.linspace(0, 360, 37)

problem = RungeKutta4(f)
problem.set_initial_condition(h0)
h, t = problem.solve(time)

plt.plot(t, h)
plt.show()
