import sys

F = 0
G = 6.674*10**(-11)

try:
    M = sys.argv[1]
    filename = sys.argv[2]
except:
    print("Enter mass and file name")
    exit()

try:
    M = float(M)
    filename = str(filename)
except:
    print("M needs to be a number")
    exit()

m = []
r = []
try:
    with open(filename, 'r') as infile:
        for line in infile:
            values = line.split()
            m.append(float(values[0]))
            r.append(float(values[1]))
except:
    print("File not found")
    exit()

for n in range(len(m)):
    F += G*M*m[n]/r[n]

print(F)
