import math

f_0 = 1
x = 1
v_0 = 2
n = 4
m = 3

v_x = math.sqrt(v_0**2+ 2*f_0/m*(math.cos(x/n)-1))

print(f"The velocity is {v_x: 2f}")
