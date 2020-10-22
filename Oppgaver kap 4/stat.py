import numpy as np
from math import sqrt

x_test_values = [0.699, 0.703, 0.698, 0.688, 0.701]

def mean(x_list):
    s = 0
    for i in range(len(x_list)):
        s += x_list[i]
    mean = s*(1/(len(x_list)))
    return mean

def test_mean():
    expected = np.mean(x_test_values)
    computed = mean(x_test_values)
    tol = 1e-10
    success = abs(expected - computed) < tol
    assert success, \
        f"expected {expected}, computed {computed}"

def standard_deviation(x_list):
    sum = 0
    for i in range(len(x_list)):
        sum += (x_list[i]-mean(x_list))**2
    s_n = sqrt((1/len(x_list))*sum)
    return s_n

def test_standard_deviation():
    x_test_values = [0.699, 0.703, 0.698, 0.688, 0.701]
    expected = np.std(x_test_values)
    computed = standard_deviation(x_test_values)
    success = expected == computed
    msg = f"Computed {computed}, expected {expected}"
    assert success, msg

test_mean()
test_standard_deviation()

"""
Terminal> python stat.py

"""
