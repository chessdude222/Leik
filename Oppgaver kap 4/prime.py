from math import sqrt

def prime(n):
    message = f"{n} is a prime"
    for i in range(2, int(sqrt(n))+ 1):
        if n%i == 0:
            message = f"{n} is not prime"
            break
        else:
            continue
    return message

#a.) for n in range(1, 101):
    #r = prime(n)
    #if r == f"{n} is a prime":
        #print(n)

def factorization(n):
    r = prime(n)
    if r == f"{n} is a prime":
        print(prime)
    factor = 2
    factors = []
    while n > 1:
        if n%factor == 0:
            factors.append(factor)
            n = n/factor
            factor = 1
        factor += 1
    return factors

def test_prime():
    n = 4
    expected = "4 is not a prime"
    computed = prime(n)
    success == expected == computed 
    assert success

def test_factorization():
    n = 8
    expected = [2, 2, 2]
    computed = factorization(n)
    success = expected == computed
    assert success
