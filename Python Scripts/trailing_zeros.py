import sys
n = int(input())
s = 0
time = 1

while n // (5**time) != 0:
    s += n // (5**time)
    time += 1


print(s, file = sys.stdout)
