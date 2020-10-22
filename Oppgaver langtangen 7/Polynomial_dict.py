class Polynomial:
    def __init__(self, exp):
        self.exp = exp

    def __call__(self, x):
        s = 0
        for i in self.exp:
            s = s + self.exp[i]*x**i
        return s

    def __add__(self, other):
        result = {}
        for exp in self.exp:
            if exp in other:
                result[exp] = self.exp[exp] + other[exp]
            else:
                result[exp] = self.exp[exp]
        for exp in other:
            if exp in result:
                pass
            else:
                result[exp] = other[exp]
        return result

p1 = Polynomial({4:1, 2:-2, 0:3})    # x^4 - 2*x^2 + 3
p2 = Polynomial({0:4, 1:3})           # 4 + 3*x
p3 = p1 + p2                # x^4 - 2*x^2 + 3*x + 7
print(p3.exp)             # prints {0: 7, 1: 3, 2: -2, 4: 1}
