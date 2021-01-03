from math import *

def diff(f,x,h):
    value = f(x)
    deriv = (f(x+h) - f(x))/h
    return value, deriv





i = [1,2,3,4]

for n in i:
    x = pi/4
    analytical = cos(x)
    h = 0.5**n
    diff = abs(diff(sin, x, h)[1] - analytical)
    print(f'{x:.3f} {h:.3f} {diff:.3f}')
