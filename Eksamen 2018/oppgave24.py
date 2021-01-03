import numpy as np

def exp_approx(x, n):
    s = 0
    for k in range(0, n+1):
        s += x**k/np.math.factorial(k)
    return s

print(exp_approx(10, 3))
