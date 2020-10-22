import math

#a) time_constant_1 = 1760
mass = 4500
time = 10*60
half_time = 1220
time_constant_2 = half_time/math.log(2)
mass_after_time = mass*math.e**(-time/time_constant_2)



#a) print(f"The mass left after {time} seconds are {mass_after_time: 2f} grams")
print(f"The mass left after {time} seconds are {mass_after_time: 2f}")
