def taylor_exp_diffeq(x, N):
    e0 = 0
    a0 = 1
    for i in range(1, N+1):
        e = e0 + a0
        a = x/i*a0
        a0 = a
        e0 = e
    return e

print(taylor_exp_diffeq(2, 100))
