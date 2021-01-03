class Poly:
    def __init__(self, dict):
        self.coeff = dict

    def __call__(self, x):
        dict = self.coeff
        s = 0
        for i in dict:
            s += dict[i]*x**i
        return s

    def __add__(self, other):
        main = self.coeff
        other = other.coeff
        new = main.copy()
        for i in other:
            if i in new:
                new[i] += other[i]
            else:
                new[i] = other[i]
        return Poly(new)

    # Oppgave 6
    def diff(self):
        coeff = self.coeff
        new = {}
        for i in coeff:
            if i == 0:
                pass
            else:
                new[i-1] = i*coeff[i]
        return Poly(new)

p1 = Poly({1:-1, 3:1})
print(p1(3))
p2 = Poly({1:3, 2:2})
p3 = p1 + p2
print(p3.coeff)

p4 = p3.diff()
print(p4.__class__.__name__)
print(p4.coeff)
