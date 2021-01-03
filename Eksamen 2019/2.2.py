from math import cos

def midpoint(f,x,h):
    exact = f(x)
    deriv = (f(x + h) - f(x-h))/(2*h)
    return exact, deriv

deriv = midpoint(cos, 0, 0.001)[1]
print(deriv)
