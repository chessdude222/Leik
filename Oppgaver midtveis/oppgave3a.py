def piecevise(x, a, b):
    if x <= a:
        return 0.0
    elif a < x and x <= b:
        return (x-a)/(b-a)
    elif x > b:
        return 1.0

def test_piecevise():
    x = [-1.0, 0.5, 1.5]
    a = 0
    b = 1
    expected = [0.0, 0.5, 1.0]
    for x, exp in zip(x, expected):
        assert piecevise(x,a,b) == exp
