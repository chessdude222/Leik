import numpy as np

def g(xp, f, dxf): # Function that calulates the differential equation
    x = xp - f(xp)/(dxf(xp))
    return x

f = np.sin      # Function
dxf = np.cos    # The derivative of the function
x_0 = 3.14      # Starting value
x = np.zeros(3) # Array with length of the values that need to be calculated
x[0] = x_0      # Fill in the intial condition

for i in range(1,3): # Fills in the array by using the function
    x[i] = g(x[i-1], f, dxf)

for n in range(len(x)): # Prints out the values in a nice table
    print(f'x{n}    = {x[n]:.13f}\nexact = {np.pi:.13f}')

"""
Terminal > python finding_pi.py
x0    = 3.1400000000000
exact = 3.1415926535898
x1    = 3.1415926549364
exact = 3.1415926535898
x2    = 3.1415926535898
exact = 3.1415926535898
"""
