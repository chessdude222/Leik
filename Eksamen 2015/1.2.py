def piecewise(x):
    if x <= 0:
        return -x
    else:
        return x

def test_piecewise():
    x = 5
    calculated = piecewise(x)
    expected = 5
    success = calculated == expected
    assert success

test_piecewise()
