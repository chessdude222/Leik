from math import sqrt

c = 300000000
v = 100000000
m = 0.14

gamma = 1/sqrt(1-(v**2/c**2))
p = m*v*gamma

print(p, gamma)
