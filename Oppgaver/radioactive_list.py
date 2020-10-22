import math
N_0 = 4500
tau = 1760
t = 0
increment = 60
r = N_0*math.e**(-t/tau)
L = []
values = []

#)a while r > 4500/2:
    #r = N_0*math.e**(-t/tau)
    #print(f"t = {t}s", f"N(t) = {r: g}kg")
    #t += increment

while r > 4500/2:
    r = N_0*math.e**(-t/tau)
    values = [t, r]
    L.append(values[:])
    values.clear()
    t += increment

for n in range(len(L)):
    print(L[n])
   
