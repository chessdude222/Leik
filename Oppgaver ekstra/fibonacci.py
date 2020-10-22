import numpy as np

def f(xp, xpp):     # Function that calulates the fibonacci number from the two previous
    x = xp + xpp
    return x

x = np.zeros(15)    # Creates an array with the correct length
x[0] = x[1] = 1     # Sets the x-values to the given starting conditions

for i in range(2, 15): # Fills the array with fibonacci numbers
    x[i] = f(x[i-1], x[i-2])

for n in x: # Loops through the calculated numbers and prints them
    print(n)

"""
Terminal > python fibonacci.py
1.0
1.0
2.0
3.0
5.0
8.0
13.0
21.0
34.0
55.0
89.0
144.0
233.0
377.0
610.0
"""
