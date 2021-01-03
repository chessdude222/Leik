def piecewise(x):
    if x < 0:
        return 0
    elif x >= 0:
        return 1

def test_piecewise():
    expected = [0 , 1]
    values = [-0.5, 0.5]
    tol = 1E-10
    for e, i in zip(expected, values):
        assert abs(e - piecewise(i)) < tol

test_piecewise()
