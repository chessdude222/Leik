import matplotlib.pyplot as plt
import numpy as np

class Quadratic:
    def __init__(self, f):
        self.f = f
        self.b = self.f(1) - self.f(0) - 1
        self.c = self.f(0)

    def compute_tangent(self, point):
        C = self.f(point) - (2*point + self.b)*point
        l = lambda x: (2*point + self.b)*x + C
        return l

    def plot_tangent(self, point):
        x = np.linspace(point - 10, point + 10, 500)
        C = self.f(point) - (2*point + self.b)*point
        l = lambda x: (2*point + self.b)*x + C
        plt.plot(x, self.f(x))
        plt.plot(x, l(x))
        #plt.show()

    def animate_plot(self, start, stop):
        plt.axis([-7.5, 7.5, -5, 30])
        x_values = np.linspace(start, stop, 100)
        s = self.compute_tangent(start)
        lines = plt.plot(x_values, s(x_values))
        plt.plot(x_values, self.f(x_values))
        for i in x_values:
            l = self.compute_tangent(i)
            y = l(x_values)
            lines[0].set_ydata(y)
            plt.draw()
            plt.pause(0.01)

s = lambda x: x**2
leik = Quadratic(s)
leik.animate_plot(-5, 5)
