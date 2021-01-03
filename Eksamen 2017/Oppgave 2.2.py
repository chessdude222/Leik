def heaviside(x):
    if x < 0:
        return 0
    elif x >= 0:
        return 1

def test_heaviside():
    calculated1 = heaviside(-1)
    calculated2 = heaviside(1)
    expected1 = 0
    expected2 = 1
    tol = 1E-8
    assert abs(calculated1 - expected1) < tol
    assert abs(calculated2 - expected2) < tol

test_heaviside()
