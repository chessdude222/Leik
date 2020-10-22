def factorization(n):
    factor = 2
    factors = []
    while n > 1:
        if n%factor == 0:
            factors.append(factor)
            n = n/factor
            factor = 1
        factor += 1
    return factors

def euler(n, m):
    n_list = factorization(n)
    m_list = factorization(m)
    r = True
    for i in range(len(n_list)):
        if n_list[i] in m_list:
            r = False
            break
    return r

def totient(d):
    L = []
    for i in range(1, d):
        if euler(i, d):
            L.append(i)
    return L

S = [10, 50, 100, 200]

#for n in S:
    #print(totient(n))

def test_euler():
    n = 6
    m = 9
    expected = True
    computed = euler(n, m)
    success = expected == computed
    assert success

def test_totient():
    d = 20
    expected = [1, 3, 7, 9, 11, 13, 17, 19]
    computed = totient(d)
    success = expected == computed
    assert success

print(euler(6, 9))
print(totient(20))
