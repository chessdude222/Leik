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

if b**2-4*a*c < 0:
    raise ValueError('Answer is not defined in the real numbers, please try something different')
else:
    print(quadratic_solver(a, b, c))

"""
Prøver eksemplene i oppgaveteksten. a = 1, b = 1, c = 1 og a = 1, b = 0,
c = −1.
Terminal > python quadratic_roots_error2.py
Enter a:
Terminal > 1
Enter b: 1
Terminal > 1
Enter c:
Terminal > 1
Traceback (most recent call last):
  File "quadratic_roots_error2.py", line 22, in <module>
    raise ValueError('Answer is not defined in the real numbers, please try something different')
ValueError: Answer is not defined in the real numbers, please try something different
Terminal > python quadratic_roots_error2.py
Enter a:
Terminal > 1
Enter b: 1
Terminal > 0
Enter c:
Terminal > -1
(1.0, -1.0)
"""
