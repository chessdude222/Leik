import matplotlib.pyplot as plt

x_list = []
y_list = []

with open('mydat.txt', 'r') as infile:
    for line in infile:
        x,y = line.split()
        x_list.append(float(x))
        y_list.append(float(y))

plt.plot(x_list,y_list)
plt.show()
