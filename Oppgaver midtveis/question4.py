def convert_velocity(v):
    miles = 1609.344
    kmh = v*(miles/1000)
    ms = kmh/3.6
    return ms, kmh

# A)
animals = []; velocities = []
with open('speeds.txt', 'r') as infile:
    infile.readline()
    infile.readline()
    for line in infile:
        values = line.split()
        animals.append(values[0])
        ms, kmh = convert_velocity(float(values[1]))
        velocities.append(ms)

# B)
animal_velocities = []
for i in range(len(animals)):
    a = [animals[i], velocities[i]]
    animal_velocities.append(a)

# C)
with open('velo_converted.dat', 'w') as outfile:
    for i in range(len(velocities)):
        outfile.write(f'{animals[i]: <20}{velocities[i]: 10.2f}\n')
