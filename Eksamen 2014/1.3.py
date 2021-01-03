"""
a)
1 0
2 0
3 0
b)
need to set inital condition
"""

# c)
import numpy as np

def difference(N):
    y = np.zeros(N+1, int)
    y[0] = 1
    for i in range(1, N+1):
        y[i] = i*y[i-1]
    return y

print(difference(14))


# d)

def test_difference():
    expected = (1,1,2,6)
    computed = difference(3)
    tol = 1E-10
    for e, c in zip(expected, computed):
        assert abs(e - c) < tol

test_difference()
