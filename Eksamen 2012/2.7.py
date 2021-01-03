import matplotlib.pyplot as plt

with open('numbers.txt', 'r') as infile:
    x = []; y = []; unc = []
    for line in infile:
        n = line.split()
        x.append(float(n[0]))
        y.append(float(n[1]))
        if len(n) == 3:
            unc.append(float(n[2]))
        else:
            unc.append(0)

points = [unc[i]*y[i] + y[i] for i in range(len(y))]

plt.plot(x,y, 'r')
plt.plot(x, points, 'bo')
plt.show()
