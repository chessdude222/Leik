
import math
B = 50000   # carrying capacity
k = 0.2     # population growth
t_0 = 0     # Start time
N_0 = 5000  # Initial population
n = 12      # Intervals
increment = (48-0)/n
N = []
t = []

C = (B/N_0-1)/math.e**(-k*t_0)

for r in range(n+1):
    N_t = int(B/(1+C*math.e**(-k*r*increment))) # Calculates the population after the increment in time
    N.append(N_t)                               # List of N values
    t.append(int(r*increment))                  # List of t values

print(" t","  N(t)")
for x in range(len(t)):
    print(f"{t[x]:2}", f"{N[x]:6}")

format_table(["t", "N"], [t, N])
"""
Kjøreeksempel:
python population_table
 t   N(t)
 0   5000
 4   9912
 8  17748
12  27526
16  36580
20  42924
24  46551
28  48389
32  49263
36  49666
40  49849
44  49932
48  49969
"""
