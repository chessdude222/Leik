import numpy as np

def RungeKutta2(f, U0, T, n):
    t = np.linspace(0, T, n+1)
    u = np.zero(len(t))
    u[0] = U0

    for k in range(len(t)-1):
        dt = t[i+1] - t[i]
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k] + 0.5*K1, t[k] + 0.5*dt)
        u[k+1] = u[k] + K2

    return t, u
