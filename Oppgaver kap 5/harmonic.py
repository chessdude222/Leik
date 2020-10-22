import sys

def f(x, N):
    s = 0
    for i in range(1, N+1):
        s += x**i/i
    return s

x = float(sys.argv[1])
N = int(sys.argv[2])

print(f(x ,N))
