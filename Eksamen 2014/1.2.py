def piecewise(t):
    if t < 5:
        return 0
    else:
        return 0.4

def test_piecewise():
    computed = piecewise(4)
    expected = 0
    tol = 1E-10
    success = abs(computed - expected) < tol
    assert success

test_piecewise()
