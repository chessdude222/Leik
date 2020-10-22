import math

def myfactorial(n):
    r  = 1
    for i in range(1,n+1):
        r = r*i
    return r

def test_myfactorial():
    n = 20
    expected = math.factorial(n)
    computed = myfactorial(n)
    success = computed == expected
    assert success

test_myfactorial()
