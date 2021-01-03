from math import sqrt

class Parabola:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        a, b, c = self.a, self.b, self.c
        return a*x**2 + b*x + c

    def roots(self):
        a, b, c = self.a, self.b, self.c
        x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
        x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
        return x1, x2

def test_Parabola():
    test = Parabola(1, 0, -1)
    expected = 0
    computed = test(1)
    tol = 1E-8
    assert abs(expected - computed) < tol
    root1, root2 = test.roots()
    expected1 = 1
    expected2 = -1
    assert abs(expected1 - root1) < tol
    assert abs(expected2 - root2) < tol

test_Parabola()
