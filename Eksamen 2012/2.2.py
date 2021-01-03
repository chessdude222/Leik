import math

class Gaussian:
    def __init__(self,m):
        self.m = m

    def __call__(self, x):
        m = self.m
        return math.exp(-0.5*(x-m)**2)/math.sqrt(2*math.pi)

f = Gaussian(m=2)
value = f(2.5)
print(values)
