import matplotlib.pyplot as plt
import numpy as np

n = 500; R0 = 100; F0 = 20 # Given values

def population(R_n, F_n, a = 0.04, b = 0.1, c = 0.005, e = 0.2): # The differencial equation described in the problem
    R = R_n + a*R_n - c*R_n*F_n
    F = F_n + e*c*R_n*F_n - b*F_n
    return R, F

foxes = np.zeros(n+1) # Start indexing at n = 0
rabbits = np.zeros(n+1)
foxes[0] = F0           # Sets the inital values
rabbits[0] = R0

for i in range(0, n): # By using the described function, loops through and fills the arrays
    rabbits[i+1], foxes[i+1] = population(rabbits[i], foxes[i])

time = np.linspace(0, 500, 501)                 # Makes the time be 500 weeks as described in the problem
plt.plot(time, rabbits, 'r', label = 'rabbits') # Plots the graphs
plt.plot(time, foxes, 'g', label = 'foxes')
plt.legend()
plt.show()

"""
Terminal > Lotka_Volterra.py
(shows a graph)
"""
