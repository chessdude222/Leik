def piecewise(x, a, b):
    if x <= a:
        return 0.0
    elif a < x and x <= b:
        return (x-a)/(b-a)
    else:
        return 1.0

print(piecewise(-1,0,1))
