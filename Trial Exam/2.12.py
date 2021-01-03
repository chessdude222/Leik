def is_prime(k):
    for i in range(2, k):
        if k % i == 0:
            return False

    return True

def primes(n):
    list = []
    s = 2
    while len(list) < n:
        if is_prime(s) == True:
            list.append(s)
        s += 1
    return list

def primeTable(k, n):
    skrrt = primes(n)
    for i in skrrt:
        print(i, end = ' ')
    print('\n')
    for k in range(k-1, 0, -1):
        skrrt = [abs(skrrt[i+1] - skrrt[i]) for i in range(k)]
        for i in skrrt:
            print(i, end = ' ')
        print("\n")

primeTable(5,5)
