def is_prime(k):
    for i in range(2, k):
        if k % i == 0:
            return False

    return True

print(is_prime(100))
