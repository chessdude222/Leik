import matplotlib.pyplot as plt

class Square:
    def __init__(self, initial):
        self.initial = initial

    def approx_frac(self, n):
        s = self.initial
        for i in range(n):
            s = 1 + 1/(1 + s)
        return s

    def approx_iter(self, n):
        x = self.initial
        for i in range(n):
            x = 0.5*(x + 2/x)
        return x

a = Square(1)
n = [1,2,5,10]

"""
print('           frac        iter         difference')
for i in n:
    s = abs(a.approx_frac(i) - a.approx_iter(i))
    print(f'n = {i:2} {a.approx_frac(i):1.10f} {a.approx_iter(i):1.10f} {s}')
"""
for i in n:
    plt.plot(i, a.approx_frac(i), 'go', label = 'frac')
    plt.plot(i, a.approx_iter(i), 'ro', label = 'iter')

plt.legend()
plt.show()
