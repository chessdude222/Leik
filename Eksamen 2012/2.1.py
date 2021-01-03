import math

def f(x):
    return math.exp(-0.5*(x-m)**2)/math.sqrt(2*math.pi)

m = 0
print(f(0.5))
