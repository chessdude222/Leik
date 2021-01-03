from math import sin

def diff(f,x,h):
    div = (f(x + h) - f(x))/h
    return f(x), div

print(diff(sin, 0, 0.001))
