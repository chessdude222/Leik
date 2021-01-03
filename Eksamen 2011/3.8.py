import numpy as np

def filereader(filename):
    with open (filename, 'r') as infile:
        x = []
        y = []
        for line in infile:
            if '#' in line:
                pass
            else:
                numbers = line.split()
                x.append(float(numbers[0][2:]))
                y.append(float(numbers[1][2:]))
    return np.array(x), np.array(y)

print(filereader('cords.txt'))
