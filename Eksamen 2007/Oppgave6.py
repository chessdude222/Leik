def position(t, v0):
    g = 9.81
    y = v0*t - 0.5*g*t**2
    deriv = v0 - g*t
    return y, deriv

v0 = 2
time = 0.1

y, y_deriv = position(time, v0)
print(y, y_deriv)
