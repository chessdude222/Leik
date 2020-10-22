import math
B = 50000   # carrying capacity
k = 0.2     # population growth
t_0 = 0     # Start time
n = 12      # Intervals
N_0 = 5000  # Starting population
increment = (48-0)/n
tN1 = []
N = []
t = []

C = (B/N_0-1)/math.e**(-k*t_0)

for r in range(n+1):
    N_t = int(B/(1+C*math.e**(-k*r*increment))) # Calculates the population after the increment in time
    N.append(N_t)                               # List of N values
    t.append(int(r*increment))                  # List of t values

tN1.append(t)
tN1.append(N)

tN2 = []

for n in range(len(N)):
    L = [t[n], N[n]]
    tN2.append(L)

for x in range(len(N)):         # oppgave a)
    print(f"{tN1[0][x]:2}", f"{tN1[1][x]: 7}")

for i in range(len(tN2)):      # oppgave b)
    print(f"{tN2[i][0]:2}", f"{tN2[i][1]: 7}")

"""
Kjøreeksempel a):
 0    5000
 4    9912
 8   17748
12   27526
16   36580
20   42924
24   46551
28   48389
32   49263
36   49666
40   49849
44   49932
48   49969
Kjøreeksempel b):
 0    5000
 4    9912
 8   17748
12   27526
16   36580
20   42924
24   46551
28   48389
32   49263
36   49666
40   49849
44   49932
48   49969
"""
