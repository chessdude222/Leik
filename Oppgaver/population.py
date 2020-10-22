import math
B = 50000 # carrying capacity
k = 0.2 # population growth
t_0 = 0 # hours
N_0 = 5000 # Initial population
t = 24 # hours

C = (B/N_0-1)/(math.e**(-k*t_0))

N_t = B/(1+C*math.e**(-k*t))

print(f"The population after {t} hours is{N_t: g}")

"""
Kjøreeksempel:
python population.py
The population after 24 hours is 46552
"""
