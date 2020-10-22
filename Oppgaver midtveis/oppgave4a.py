def pi_approx(n):
    s = 0
    for k in range(1, n+1):
        s += (-1)**(k+1)/(2*k-1)
    return s*4

print(pi_approx(10), pi_approx(100))
