class MinMax:
    def __init__(self, f, a, b, n):
        self.f = f
        self.a = a
        self.b = b
        self.n = n
        self.h = (b-a)/n
        self.p_min = []
        self.p_max = []
        self.f_min = []
        self.f_max = []

    def find_extrema(self):
        if self.f(self.a) < self.f(self.a + self.h):
            self.p_min.append(self.a)
            self.f_min.append(self.f(self.a))
        elif self.f(self.a) > self.f(self.a + self.h):
            self.p_max.append(self.a)
            self.f_max.append(self.f(self.a))
        if self.f(self.b) < self.f(self.b - self.h):
            self.p_min.append(self.b)
            self.f_min.append(self.f(self.b))
        elif self.f(self.b) > self.f(self.b - self.h):
            self.p_max.append(self.b)
            self.f_max.append(self.f(self.b))
        for i in range(1, self.n):
            if self.f(self.a + self.h*i) > self.f(self.a + self.h*(i-1)) and self.f(self.a + self.h*i) > self.f(self.a + self.h*(i+1)):
                self.p_max.append(self.a + self.h*i)
                self.f_max.append(self.f(self.a + self.h*i))
            elif self.f(self.a + self.h*i) < self.f(self.a + self.h*(i-1)) and self.f(self.a + self.h*i) < self.f(self.a + self.h*(i+1)):
                self.p_min.append(self.a + self.h*i)
                self.f_min.append(self.f(self.a + self.h*i))

    def get_global_minimum(self):
        a = min(self.f_min)
        b = self.f_min.index(a)
        return (self.p_min[b], self.f_min[b])

    def get_global_maximum(self):
        a = max(self.f_max)
        b = self.f_max.index(a)
        return (self.p_max[b], self.f_max[b])

    def get_all_minima(self):
        l = []
        for i in range(len(self.p_min)):
            temp = [self.p_min[i], self.f_min[i]]
            l.append(temp)
        return l

    def get_all_maxima(self):
        list = []
        for i in range(len(self.p_max)):
            temp = [self.p_max[i], self.f_max[i]]
            list.append(temp)
        return list

    def __str__(self):
        self.find_extrema()
        z, u = self.get_global_minimum()
        y, i = self.get_global_maximum()
        return f'All minima:{self.p_min}\nAll maxima:{self.p_max}\nGlobal minimum:{z} \nGlobal maximum:{y}\n'

from math import exp, sin, pi
def f(x):
    return x**2*exp(-0.2*x)*sin(2*pi*x)
m = MinMax(f, 0, 4, 5001)
print(m)
