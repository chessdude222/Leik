class Quadratic:
    def __init__(self, list):
        self.list = list
        self.a = list[0]
        self.b = list[1]
        self.c = list[2]

    def __call__(self, x):
        a, b, c = self.a, self.b, self.c
        return c*x**2+b*x+a

    def __str__(self):
        a, b, c = self.a, self.b, self.c
        return f'{c}x**2 + {b}x + {a}'

class Cubic(Quadratic):
    def __init__(self, list):
        super().__init__(list)
        self.d = list[3]

    def __call__(self, x):
        d = self.d
        return super().__call__(x) + d*x**3

    def derivative(self):
        self.list = self.list[1:]
        derivative = []
        for i in range(len(self.list)):
            a = (i+1)*self.list[i]
            derivative.append(a)
        return Quadratic(derivative)



test = Cubic([1,3,2,4])
print(test(1), test(2), test.derivative())
