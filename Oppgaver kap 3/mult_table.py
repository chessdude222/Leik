n = 1
L = []

while n <= 10:
    for r in range (1,11):
        t = (f'{r}*{n}')
        L.append(t)
    n += 1

print(L)
