def solve(n, p, x0):
    x_n = x0
    for i in range(n):
        next = x_n + p/(100*360)*x_n
        x_n = next
    return next

print(solve(720, 4, 100))
