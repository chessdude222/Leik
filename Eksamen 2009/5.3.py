import numpy as np

def f(N,s):
    v_temp = s
    w_temp = 0
    for i in range(1, N+1):
        v = v_temp + w_temp
        w = w_temp + d*(A*np.sin(c*(i-1)*d)) - p*abs(w_temp)*w_temp- q*np.sin(v_temp)
        v_temp = v
        w_temp = w
    return v, w

A = 2; d = 1; c = 7; q = 2; p = 1
print(f(10,2))
