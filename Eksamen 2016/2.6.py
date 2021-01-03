def f(x):
    if x < 0:
        return 0
    elif 0 <= x and x < 2:
        return x**2
    elif x >= 2:
        return 4

print(f(2))
