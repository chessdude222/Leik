with open('data.txt', 'r') as infile:
    year = []
    mean_temp = []
    max_temp = []
    min_temp = []
    infile.readline()
    for line in infile:
        values = line.split()
        year.append(values[1])
        mean_temp.append(values[2])
        min_temp.append(values[3])
        max_temp.append(values[4])
