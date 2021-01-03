import matplotlib.pyplot as plt
import numpy as np

def exp_approx(x, n):
    s = 0
    for k in range(0, n+1):
        s =  s + x**k/np.math.factorial(k)
    return s

def plot_approx(n_values):
    x = np.linspace(0, 5, 11)
    for i in n_values:
        plt.plot(x, exp_approx(x, i), label = f'i = {i}')
    plt.plot(x, np.exp(x), label = 'exact')
    plt.legend()
    plt.show()

plot_approx([1,3,5,100])
