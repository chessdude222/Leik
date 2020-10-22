import numpy as np
import matplotlib.pyplot as plt
import sys

# Oppgave a
class RightTriangle:
    def __init__(self, a, b):
        if a <= 0 or b <= 0: # Checks if a or b is negativ or 0, and raises ValueError if that is the case
            raise ValueError
        self.a = a
        self.b = b
        self.c = np.sqrt(self.a**2+self.b**2) # Calculates the c from pythagoras

    def plot_triangle(self):
        plt.plot([0,0], [0,self.b], 'g')        # Plots along the x-axis
        plt.plot([self.a,0], [0,0], 'g')        # Plots along the y-axis
        plt.plot([0, self.a], [self.b, 0], 'g') # Plots the hypotenuse
        plt.axis('equal')
        plt.show()
# Oppgave b
triangle1 = RightTriangle(1,1)
triangle2 = RightTriangle(3,4)
print(triangle1.c, triangle2.c) # Prints the c-value for the two triangles

# Oppgave c
def test_RightTriangle():
    success = False
    try:
        triangle3 = RightTriangle(1,-1)
    except ValueError:
        success = True
    assert success

test_RightTriangle()

# Oppgave d
triangle2.plot_triangle()

"""
Terminal > right_triangle.py
1.4142135623730951 5.0
(Shows a graph)
"""
