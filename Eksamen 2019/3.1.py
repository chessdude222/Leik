class F:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        a, b, c = self.a, self.b, self.c
        return a*x**2 + b*x + c

f = F(a=1.0, b=2.0, c=0.0)
x = 2.0
print(f(x))
