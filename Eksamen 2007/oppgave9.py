from math import sin, pi

class SineFunc:
    def __init__(self,p,q,r):
        self.p = p
        self.q = q
        self.r = r

    def __call__(self, t):
        p, q, r = self.p, self.q, self.r
        return sin(pi*t) + p*sin(q*pi*t) + r*sin(4*q*pi*t)

f = SineFunc(p=0.1, q=4, r=0.05)
for t in [0.2, 0.4, 1, 2]:
    f_value = f(t)
    print('f(%g)=%g' % (t, f_value))
