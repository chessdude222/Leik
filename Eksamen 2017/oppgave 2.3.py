def diff(f,x,h):
    value = f(x)
    deriv = (f(x+h) - f(x))/h
    return value, deriv
