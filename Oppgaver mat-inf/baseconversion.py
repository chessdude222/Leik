from math import floor

def digits(a, beta):
    i = 0
    L = []
    while a > 0:
        d_i = a%beta
        L.append(d_i)
        a = a // beta
    return L

def decimal_digits_fractional(a, beta, n):
    L =[]
    for n in range(-1, -n, -1):
        d_1 = floor(a*beta)
        L.append(d_1)
        a = a * beta - d_1
    return L

def decimal_digits_rational(b , c ,beta):
    i = -1
    bs = []
    while i > -1000:
        d_1 = (b*beta)//c
        bs.append(d_1)
        b = (b*beta)%c
        if (b in bs):
            print("b in bs")
            break
        elif b == 0:
            print("b = 0")
            break
        i -= 1
    return bs

print(decimal_digits_rational(21312, 5, 7))
