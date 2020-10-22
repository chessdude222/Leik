from math import sqrt

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

a = float(input("Enter a: "))   # Take input for a
b = float(input("Enter b: "))   # Take input for b
c = float(input("Enter c: "))   # Take input for c

print(quadratic_solver(a, b, c))

"""
Velger x**2+4x+4=0 som eksempel, da blir a = 1, b = 4, c = 4
Terminal > python quadratic_roots_input.py
Enter a:
Terminal> 1
Enter b:
Terminal > 4
Enter c:
Terminal > 4
-2.0
"""
