import math
v = 0
m = 1200
c = 3*10**8

while v < 0.9*10**8:
    print(f"v = {v}m/s", f"p_k = {m*v: g}kgm/s", f"p_r = {m*v*1/(math.sqrt(1-v**2/c**2)): g}")
    v += 0.1*10**8
