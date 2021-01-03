def harmonic2(n):
    s = sum([1/i for i in range(1, n+1)])
    extra = 1/(n+1)
    return s, extra

print(harmonic2(2))
