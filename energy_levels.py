m_e = 9.1094*10**-31
e = 1.6022*10**-19
e_0 = 8.8542*10**-12
h = 6.6261*10**-34

#E_list = []
for n in range(1, 21):
    E = m_e*e**4/(8*e_0*h**2)*1/n**2
    #E_list.append(E)
    #print(f"The energy level is {E: g} for level {n}")

change = []
temp = []
for i in range(1,6):
    for f in range(1,6):
        E = f"{-m_e*e**4/(8*e_0**2*h**2)*(1/i**2-1/f**2): e}"
        temp.append(E)
    change.append(temp[:])
    temp.clear()


for n in range(5):
        print(change[n])
