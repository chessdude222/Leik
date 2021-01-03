def poly_diff(p):
    new = {}
    for i in p:
        if i == 0:
            pass
        else:
            new[i-1] = p[i]*i
    return new

p = {0:1,2:-2,4:3,5:1}
print(poly_diff(p))
