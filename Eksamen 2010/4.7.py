from ODEsolver import *
import matplotlib.pyplot as plt

def f(u,t):
    x, y = u
    x_d = y/Y - x/X
    y_d = x/X - y/Y
    return [x_d, y_d]

X = 480; Y = 2400
time = np.linspace(0, 3000, 301)
problem = RungeKutta4(f)
problem.set_initial_condition([1,1])
u, t = problem.solve(time)
x = u[:,0]; y = u[:,1]

plt.plot(t,y,'b')
plt.plot(t,x,'r')
plt.show()
