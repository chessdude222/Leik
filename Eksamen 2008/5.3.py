class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __call__(self, t):
        x0, y0, x1, y1 = self.p1[0], self.p1[1], self.p2[0], self.p2[1]
        y = lambda x: y0 + (y1-y0)/(x1-x0)*(x - x0)
        return y(t)


point1 = (0,-1)
point2 = (2,4)
line = Line(point1, point2)
print(line(0))
print(line(1))
