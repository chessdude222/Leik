from math import pi

light_year = 9.5*10**15
AU = 1.58*10**-5*light_year
G = 6.674*10**-11
yr = 3.15576*10**7

solar_mass = 4*pi**2*AU**3/(G*yr**2)

print(f"The solar mass is {solar_mass:g}")
