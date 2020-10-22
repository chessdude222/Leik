class Quadratic:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def value(self, x):
        return self.a*x**2 + self.b*x + self.c

    def roots(self):
        import math
        if math.sqrt(self.b**2-4*self.a*self.c) == 0:
            return -self.b/(2*self.a)
        else:
            x_1 = (-self.b - math.sqrt(self.b**2- 4*self.a*self.c))/(2*self.a)
            x_2 = (-self.b + math.sqrt(self.b**2- 4*self.a*self.c))/(2*self.a)
            return x_1, x_2

    def table(self, n, L, R):
        import numpy
        x_values = numpy.linspace(L, R, n)
        print("    x             f")
        for i in x_values:
            print(f'{i:10.2f}      {self.value(i):.3f}')
        return ""

def test_Quadratic():
    a = Quadratic(1, 4, 4)
    assert a.value(1) == 9
    assert a.roots() == -2
