class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.f = lambda x: ((self.p2[1] - self.p1[1])/(self.p2[0] - self.p1[0]))*(x - self.p2[0]) + self.p2[1]

    def value(self, x):
        return self.f(x)
