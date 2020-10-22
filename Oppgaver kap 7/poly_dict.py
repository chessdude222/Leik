def sum(f, g):
    sum = {}
    sum1 = {}
    for i in f:
        if i in g:
            sum1[i] = (f[i] + g[i])
        else:
            sum1[i] = f[i]
    for n in g:
        if n in f:
            pass
        else:
            sum1[n] = g[n]
    order = sorted(sum1, reverse=True)

    for i in order:
        sum[i] = sum1[i]
    return sum

f = {2:3, 0:1/2}
g = {7:3, 3:5, 2:4, 0:4}

print(sum(f,g))
