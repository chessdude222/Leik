with open('constants.txt', 'r') as infile:
    dict = {}
    infile.readline()
    infile.readline()
    for line in infile:
        master = line.split()
        name = ' '.join(master[0:2])
        dict[name] = (float(master[2]), master[3])

print(dict)
