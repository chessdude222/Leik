import numpy as np

def f(N,s):
    v = np.zeros(N+1)
    w = np.zeros(N+1)
    v[0] = s
    w[0] = 0
    for i in range(1, N+1):
        v[i] = v[i-1] + d*w[i-1]
        w[i] = w[i-1] + d*(A*np.sin(c*(i-1)*d)) - p*abs(w[i-1])*w[i-1] - q*np.sin(v[i-1])
    return v, w

A = 2; d = 1; c = 7; q = 2; p = 1
