def binomial(n, i):
    s = 1.0
    for j in range(1, int(i+1)):
        if j%2 == 0:
            s = s*(n-j+1)/j
        else:
            s = s*(n-(i-j)+1)/(i-j)
    return s


#print(type(binomial(500, 4)))
#print(f"{binomial(1000, 500)}")
print(f"{binomial(100000, 99940)}")
a = binomial(100000, 99940)
