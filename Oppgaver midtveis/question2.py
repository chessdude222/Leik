Clist1 = []
F = 0
while F < 40:
    Clist1.append((F-32)*5.0/9)
    F += 5

Clist2 = []
for F in range(0, 40, 5):
    Clist2.append((F-32)*5.0/9)

print(Clist1, Clist2)
