from ODEsolver import *

def f(u, t):
    x1, x2 = u
    return [x2, np.cos(t) + 5*np.sin(x2) - 2*x1**2]

initial = [1, 0]
time = [0, 0.1, 0.2]
problem = ForwardEuler(f)
problem.set_initial_condition(initial)
u, t = problem.solve(time)
print(u)
