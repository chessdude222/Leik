class Vector2D:
    def __init__(self, vector):
        self.vector = vector
        self.x = vector[0]
        self.y = vector[1]

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2D((x, y))

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector2D((x, y))

    def __str__(self):
        return f'{self.vector}'

    def dot(self, other):
        return self.x*other.x + self.y*other.y

class Vector3D(Vector2D):
    def __init__(self, vector):
        super().__init__(vector)
        self.z = vector[2]

    def __add__(self, other):
        D2 = super().__add__(other)
        x, y = D2.x, D2.y
        z = self.z + other.z
        return Vector3D((x,y,z))

    def __sub__(self,other):
        D2 = super().__sub__(other)
        x, y = D2.x, D2.y
        z = self.z - other.z
        return Vector3D((x,y,z))

    def dot(self, other):
        return super().dot(other) + self.z*other.z

    def cross(self, other):
        a_1, a_2, a_3 = self.x, self.y, self.z
        b_1, b_2, b_3 = other.x, other.y, other.z
        c_1 = a_2*b_3 - a_3*b_2
        c_2 = a_3*b_1 - b_3*a_1
        c_3 = a_1*b_2 - b_1*a_2
        return Vector3D((c_1, c_2, c_3))

v = Vector3D((2,0,0)); w = Vector3D((0,2,0))
print(v.cross(w))
