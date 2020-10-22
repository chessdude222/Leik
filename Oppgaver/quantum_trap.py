sum = 0
h = 6.626*10**-34
mass = 9.11*10**-31
length = 10**-11
n = 2
e_last = 0
e_current = 0
jumps = 50
energy = 0
L = []

while n <= jumps:
    e_last = (n-1)**2*h**2/(8*mass*length**2)
    e_current = n**2*h**2/(8*mass*length**2)
    energy = e_current - e_last
    L.append(energy)
    n += 1

for r in range(len(L)):
    sum += L[r]

print(sum)
