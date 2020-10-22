import numpy as np
import matplotlib.pyplot as plt

# Defines the function
def y(t, k = 4, delta = 0.15, m = 9, A = 0.3):
    return A*np.exp(-delta*t)*np.cos(np.sqrt(k/m)*t)

# A)
t_array1 = np.zeros(101)    # Creates the array filled with zeros
y_array1 = np.zeros(101)

step = 25/100               # How much t needs to increase for every iteration in the for loop

for i in range(101):
    t_array1[i] = step*i
    y_array1[i] = y(step*i)

# B)
t_array2 = np.linspace(0, 25, 101)  # Creates the t-values
y_array2 = y(t_array2)              # Creates the y-values

# C)
plt.plot(t_array1, y_array1, 'r', label = 'for loop')   # Plots the values from the for loop with a red color
plt.plot(t_array2, y_array2, 'g', label = 'vectorized') # Plots the values from the vectorized code with a green color
plt.xlabel('t')
plt.ylabel('y')
plt.legend()                    # Makes the label show up
plt.axis([-1, 26, -0.5, 0.6])   # Defines the max and min values for x and y
plt.show()                      # Show the plot
"""
Terminal > python oscilliating_spring.py
(Shows a plot, were you can only see a single line.
This means the values from the two methods are identical.
Delivered the plot as Plot_oscillating_spring.png.)

"""
