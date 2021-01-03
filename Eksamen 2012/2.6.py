# File name is numbers.txt

import matplotlib.pyplot as plt

with open('numbers.txt', 'r') as infile:
    x = []; y = []
    for line in infile:
        n = line.split()
        x.append(float(n[0]))
        y.append(float(n[1]))

plt.plot(x,y, 'r')
plt.show()
