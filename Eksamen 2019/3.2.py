import numpy as np

def heun3(f, U0, T, n):
    u = np.zeros(n + 1)
    t = np.linspace(0, T, n+1)
    u[0] = U0
    dt = T/n

    for k in range(1, n+1):
        k1 = dt*f(u[k-1], t[k-1])
        k2 = dt*f(u[k-1] + k1/3, t[k-1] + dt/3)
        k3 = dt*f(u[k-1] + 2*k2/3, t[k-1] + 2*dt/3)
        u[k] = u[k-1] + k1/4 + 3*k3/4

    return u, t

f = lambda u,t: 2
print(heun3(f, 1, 10, 100))
