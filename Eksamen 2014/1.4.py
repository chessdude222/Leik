def polyeval(x, p):
    s = 0
    for i in p:
        s += p[i]*x**i
    return s

print(polyeval(2, {1:-1, 3:1}))

def polyadd(p, q):
    if len(p) > len(q):
        new = p.copy()
        for i in q:
            if i in p:
                new[i] += q[i]
            else:
                new[i] = q[i]
    else:
        new = q.copy()
        for i in p:
            if i in q:
                new[i] += p[i]
            else:
                new[i] = p[i]

    return new

print(polyadd({1:-1, 3:1}, {1:3, 2:2}))
