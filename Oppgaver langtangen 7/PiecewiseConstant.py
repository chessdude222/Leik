import numpy as np

class PiecewiseConstant:
    def __init__(self, conditions, xmax):
        self.conditions = conditions
        self.xmax = xmax

    def piece(self, x):
        if x >= self.conditions[-1][1]:
            return self.conditions[-1][0]
        elif x <= self.conditions[0][1]:
            return self.conditions[0][0]
        else:
            for i in range(1, len(self.conditions)):
                if x >= self.conditions[i-1][1] and x <= self.conditions[i][1]:
                    return self.conditions[i-1][0]

    def __call__(self, x):
        a = np.vectorize(self.piece)
        return a(x)

    def plot(self):
        b = np.vectorize(self.piece)
        a = b(self.conditions)
        return self.conditions, a


f = PiecewiseConstant([(0.4, 1), (0.2, 1.5), (0.1, 3)], xmax=4)
x = np.linspace(0, 4, 21)
print(f(x))
x, y = f.plot()
from matplotlib.pyplot import plot, show
plot(x, y, 'go')
show()
