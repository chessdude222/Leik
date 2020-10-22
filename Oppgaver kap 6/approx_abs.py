import numpy as np
import matplotlib.pyplot as plt

def f(x, N):
    s = 0
    for i in range(1, int(N+1)): # Calculates the sum
        s = s + np.cos((2*i-1)*x)/(2*i-1)**2
    return np.pi/2 - 4/np.pi*s

def exact(x): # Defines the exact function for abs(x)
    return np.abs(x)

N = np.linspace(1, 4, 4)            # Creates and array with the N values
x = np.linspace(-np.pi, np.pi, 200) # Creates the array with x-values in the given interval

for i in N:
    y = f(x, i) # Updates the y-values with a new N
    plt.plot(x, y, label = f'N = {i}')  # Plots the updated function

plt.plot(x, exact(x), label = 'exact') # Plots the exact function
plt.axis([-np.pi, np.pi, 0, np.pi+1])
plt.legend() # Shows label
plt.show()

"""
Terminal > python approx_abs.py
(Shows a graph)
"""
