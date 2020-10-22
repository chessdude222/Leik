"""
                            cost  available
    P1 P2   P1 = 150    M1 = 10,  100
M1  2  1    P2 = 175    M2 = 17,  80
M2  5  3                M3 = 25,  150
M3  0  4

x = P1      y = P2, Calculates profit minus cost

f(x, y) = 150*x - (10*2 + 17*5)*x + 175*y - (10*1 + 17*3 + 25*4)*y
f(x, y) = 150x - 105x + 175y - 161y = 45x + 14y

maximize f(x, y)
subject to:
    2x + y <= 100
    5x + 3y <= 80
    4y <= 150
    x >= 0, y >= 0

takes into account total materials
"""
import matplotlib.pyplot as plt
import sys
import numpy as np

def calculate(x, y):
    x = 45*x; y = 14*y
    return x,y

for x in range(60):
    for y in range(40):
        if 2*x + y <= 100 and 5*x + 3*y <= 80 and 4*y <= 150:
            pass
            #plt.plot(x, y, 'ro')

for i in sys.argv[1:]:
    z = eval(i[2:-2])
    a = z[0]; b = z[1]; c=z[2]
    x = np.linspace(0, 60, 100)
    y = ((-x*a+c)/b)
    #plt.plot(x,y)

p = 45; q = 14
def f(x, y):
    return p*x + q*y

x_1 = np.linspace(0, 10, 100)
for x_value in range(60):
    for y in range(40):
        if 2*x_value + y <= 100 and 5*x_value + 3*y <= 80 and 4*y <= 150:
            teta = f(x_value, y)
            y_f = lambda x: teta/p - p*x/q
            y_v = y_f(x_1)
            plt.plot([x_value, teta], [y, teta])


plt.show()
