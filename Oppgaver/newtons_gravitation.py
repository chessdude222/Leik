import math
G = 6.674*10**-11
M = 3
number = 1
number_objects = 10
force = 0
r = 0
L = []
sum = 0

while number <= number_objects:
    m = number/6+2
    r = math.sqrt((number/4)**2+10)
    force = G*m*M/r
    L.append(force)
    number += 1

s = [1,2,4,6]
print(math.fsum(L))
