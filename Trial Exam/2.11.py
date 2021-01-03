def is_prime(k):
    for i in range(2, k):
        if k % i == 0:
            return False

    return True

def primes(n):
    list = []
    s = 3
    while len(list) <= n:
        if is_prime(s) == True:
            list.append(s)
        s += 1
    return list

print(primes(100))
