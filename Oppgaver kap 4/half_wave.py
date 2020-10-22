from math import sin, pi, sqrt

def f(x):
    if sin(x) > 0:
        f = sin(x)
    else:
        f = 0
    return f

def test_f():
     x_vals = [7*pi/4, pi/4]
     expected_values = [0, sqrt(2)/2]
     tol = 1e-10
     for x, exp in zip(x_vals, expected_values):
         assert abs(f(x)-exp) < tol, f'Failed for x = {x}, expected {exp}, but got {f(x)}'

test_f()

"""
Terminal > python half_wave.py

"""
