import math

a = 6 # x**2
b = -5 # x
c = 1

x_1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
x_2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)

print(f"x_1 ={x_1: .2f}, x_2 ={x_2: .2f}")

"""
Kjøreeksempel:
python find_roots.py
x_1 = 0.50, x_2 = 0.33
"""
