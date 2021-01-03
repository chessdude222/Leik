import matplotlib.pyplot as plt

with open('test.txt', 'r') as infile:
    x = []; y = []
    for line in infile:
        x_v, y_v = line.split()
        x_v = x_v.strip()
        y_v = y_v.strip()
        x.append(float(x_v))
        y.append(float(y_v))

plt.plot(x, y)
plt.show()
