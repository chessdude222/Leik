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
try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
except IndexError:
        print("Missing input")
        # Checks the number of inputs, and asks for the missing ones, if there is too many prints it and exits
        if len(sys.argv) == 1:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))
        elif len(sys.argv) == 2:
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))
        elif len(sys.argv) == 3:
            c = float(input("Enter c: "))
        else:
            print("Too many inputs")
            exit()

print(quadratic_solver(a, b, c))

"""
Prøver å skrive inn hverken a,b eller c. Og deretter skrive a = 1, b = 8, c = 4
Terminal > python quadratic_roots
Missing input
Enter a:
Terminal > 1
Enter b:
Terminal > 8
Enter c:
Termnial > 4
(-0.5358983848622456, -7.464101615137754)
"""
