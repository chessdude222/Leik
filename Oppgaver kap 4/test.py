def addition(x, y):
    sum = x+y
    return sum

def test_addition():
    x = 3
    y = 4
    expected = 5
    computed = addition(x, y)
    success = expected == computed
    assert 5 == 7

test_addition()
