from math import factorial

def cos_approx(x, n):
    s = 0
    for k in range(n+1):
        s += (-1)**k*x**(2*k)/(2*factorial(k))
    return s
