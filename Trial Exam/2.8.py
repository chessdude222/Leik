def harmonic(n):
    s = sum([1/i for i in range(1, n+1)])
    return s

print(harmonic(2))
