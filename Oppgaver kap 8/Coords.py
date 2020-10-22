from math import sqrt

class Coords:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return (f'({self.x:.2f} {self.y:.2f} {self.z:.2f})')

    def __len__(self):
        l = [self.x, self.y, self.z]
        return len(l)

    def __abs__(self):
        x, y, z = self.x, self.y, self.z
        return sqrt(x**2 + y**2 + z**2)

    def __add__(self, other):
        x_1, y_1, z_1 = other.x, other.y, other.z
        x_2, y_2, z_2 = self.x, self.y, self.z
        self.x = x_1 + x_2
        self.y = y_1 + y_2
        self.z = z_1 + z_2
        return self

    def __sub__(self, other):
        x_1, y_1, z_1 = other.x, other.y, other.z
        x_2, y_2, z_2 = self.x, self.y, self.z
        self.x = x_1 - x_2
        self.y = y_1 - y_2
        self.z = z_1 - z_2
        return self


sqrt3 = sqrt(3)
close = Coords(1/sqrt3, 1/sqrt3, 1/sqrt3)
far = Coords(3/sqrt3, 15/sqrt3, 21/sqrt3)

further = close + far
print(f"The coordinates further are at {further}")
distance = abs(far - close)
print(f"The distance from far to close is {distance}")
centre = further - further
print(f"The coordinates at the centre are {centre}")
