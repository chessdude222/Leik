import numpy as np
import matplotlib.pyplot as plt

def pi_approx(n):
    s = 0
    for k in range(1, int(n+1)):
        s += (-1)**(k+1)/(2*k-1)
    return s*4

n = np.linspace(1, 50, 50)
v_pi = np.vectorize(pi_approx)
y = v_pi (n)
plt.plot(n, y)
plt.show()
