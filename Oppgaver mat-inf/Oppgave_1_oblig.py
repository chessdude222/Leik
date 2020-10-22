from math import sqrt

def equation(x_0, x_1, n):
    """
    Function that calculates the differential equation x_(n+2) − 4x_(n+1) − x_n = 0
    And that takes the inputs: first and second value defined by x_0, x_1,
    and number of the item you wish to return defined by n.
    """
    for i in range(n-1):
        x = x_0 + x_1*4
        x_0 = x_1
        x_1 = x
    return x

def analytic(n):
    return (2-sqrt(5))**(n)

for n in range(2, 101):
    print(f"x{n} = {(equation(1, 2-sqrt(5), n))}, {analytic(n)}")

def test_equation(n):
    feil = 0
    tol = 1e-12
    for i in range(2, n+1):
        if abs(analytic(i) - equation(1, (2-sqrt(5)), i)) < tol:
            pass
        else:
            feil += 1
    return 100 * feil/n
