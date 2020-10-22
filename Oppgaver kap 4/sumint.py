def sumint(n):
    s = 0
    for i in range(1,n+1):
        s += i
    return s

def sumint_formula(n):
    a = n*(n+1)/2
    return a

def test_sumint():
    n = 5
    expected = 15
    computed = sumint(n)
    success = computed == expected
    assert success

def test_sumint_formula():
    n = 5
    expected = 15
    computed = sumint_formula(5)
    success = expected == computed
    assert success

test_sumint()
test_sumint_formula(y)
