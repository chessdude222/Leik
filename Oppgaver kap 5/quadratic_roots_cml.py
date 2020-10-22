from math import sqrt
import sys

def quadratic_solver(a, b, c):
    """
    Quadratic equation solver that takes inputs a,b,c
    and doesn't work for complex numbers
    """
    tol = 1e-12
    if abs(b**2-4*a*c) < tol: # Could write == 0, but since we are subtracting i define a tolerance
        x_1 = -b/(2*a)
        return x_1
    else:
        x_1 = (-b+sqrt(b**2-4*a*c))/2*a
        x_2 = (-b-sqrt(b**2-4*a*c))/2*a
        return x_1, x_2

a = float(sys.argv[1])  # Takes the a value from input
b = float(sys.argv[2])  # Takes the b value from input
c = float(sys.argv[3])  # Takes the c value from input

print(quadratic_solver(a, b, c))

"""
Inputtene skal skrives inn i rekkefølgen: a,b,c.
Prøver eksempelet: x**2+16x+2=0. Da blir a = 1, b = 16, c = 2
Terminal > python quadratic_roots_cml.py 1 16 2
(-0.12599212598818887, -15.874007874011811)
"""
