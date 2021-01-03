import sys
import math

class Gaussian:
    def __init__(self,m):
        self.m = m

    def __call__(self, x):
        m = self.m
        return math.exp(-0.5*(x-m)**2)/math.sqrt(2*math.pi)

try:
    m = float(sys.argv[1])
except:
    print('m needs to be supplied and be a number')
    exit()

try:
    x = [float(i) for i in sys.argv[2:]]
except:
    print('x needs to be one or more values and numbers')
    exit()

f = Gaussian(m)
for n in x:
    print(f'{f(n):e}')
