class Central:
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = h

    def __call__(self, x):
        return (self.f(x + self.h) - self.f(x - self.h))/(2*self.h)

def f(x):
    return 0.25*x**4

df = Central(f)
x = 2
print(f'df({x})={df(x)}')
print('exact', x**3)
