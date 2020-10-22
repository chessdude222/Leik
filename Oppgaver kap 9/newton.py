class Diff:
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

    def diff1(self, x):
        h, f = self.h, self.f
        return (f(x+h) - f(x))/h

    def diff2(self, x):
        h, f = self.h, self.f
        return (f(x+h)-f(x-h))/(2*h)

    def diff3(self, x):
        h, f = self.h, self.f
        return (-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)

class Function(Diff):
    def __call__(self, x):
        return self.f(x)

    def approx_root(self, start, epsilon):
        if epsilon <1:
            for i in range(1000):
                start = start - self.f(start)/self.diff3(start)
                if self.f(start) < epsilon:
                    return start
                else:
                    continue
                if i == 100:
                    if self.f(start) < 1:
                        continue
                    else:
                        print('not convergent')
                        break
        else:
            print('epsilon too large, needs to be less then 1')
            exit()

def f(x):
    return x**2 -1

func = Function(f)

from math import pow
i = [1,2,3,4,5,6]

for n in i:
    x = func.approx_root(5, pow(10, -n))
    print(f'{x}, {f(x)}')
