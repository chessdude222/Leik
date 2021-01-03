from math import pi, sin

class SineFunc:
    def __init__(self,p,q,r):
        self.p = p
        self.q = q
        self.r = r

    def __call__(self, t):
        p, q, r = self.p, self.q, self.r
        return sin(pi*t) + p*sin(q*pi*t) + r*sin(4*q*pi*t)

f = SineFunc(p=0.5, q=3, r=0.05)


def table(f, a, b, n, filename):
    h = (b - a)/(n-1)
    with open(filename, 'w') as outfile:
        for i in range(n):
            x = a + i*h
            y = f(x)
            outfile.write(f'{x} ')
            outfile.write(f'{y}\n')

table(f, 0, pi, 31, 'mydat.txt')
