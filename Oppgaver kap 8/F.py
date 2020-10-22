import numpy as np
import matplotlib.pyplot as plt

class F:
    def __init__(self, n, m): # Defines the constructor with the given parameters
        self.n = n
        self.m = m

    def __call__(self, x):
        n, m = self.n, self.m          # Renames the parameters
        return np.sin(n*x)*np.cos(m*x)  # Defines the given function

u = F(10, 20)                        # Creates the instance u
v = F(7, 13)                         # Creates the instance v
x = np.linspace(0, 2*np.pi, 1000)    # Creates the x-values

plt.plot(u(x), v(x))                 # Plots the u on x-axis, and v on y-axis
plt.show()


"""
Terminal > F.py
(shows a graph)
"""
