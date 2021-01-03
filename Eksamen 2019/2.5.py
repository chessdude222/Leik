def poly_eval(p, x):
    s = 0
    for i in p:
        s += p[i]*x**i
    return s

p = {0:1,2:-2,4:3,5:1}
print(poly_eval(p, 1000))
