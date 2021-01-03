import numpy as np

def maxima(x, y):
    maxes = []
    distances = []

    if y[0] > y[1]:
        maxes.append(y[0])
        last_max = x[0]
    else:
        last_max = 0

    for k in range(1, len(y)-1):
        if y[k] > y[k-1] and y[k] > y[k+1]:
            maxes.append(y[k])
            distances.append(x[k] - last_max)
            last_max = x[k]

    if y[-1] > y[-2]:
        maxes.append(y[-1])
        distances.append(x[k] - last_max)

    return maxes, distances

def test_maxima():
    f = np.sin
    x_values = np.linspace(np.pi/2, np.pi*13/2, 400)
    y_values = f(x_values)
    expected_value = 1
    expected_distance = 2*np.pi
    computed, distance = maxima(x_values, y_values)
    tol = 1E-8
    for e_ in computed:
        assert abs(e_ - expected_value) < 0.1, f'e_ = {e_}'
    for e_ in distance:
        assert abs(expected_distance - e_) < 0.1, f'e_ = {e_}'

test_maxima()
