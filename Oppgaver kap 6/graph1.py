import numpy as np
import matplotlib.pyplot as plt

# Oppgave a)
def plot_line(p1, p2):
    plt.plot(p1[0], p1[1], 'go', label = 'p1')    # Plots the points
    plt.plot(p2[0], p2[1], 'ro', label = 'p2')
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'm') # Plots the line from filling in the x- and y-value to the two points

p1_h = (0, 0)
p2_h = (-5, 0)
p1_v = (-1, -1)
p2_v = (-1, -5)

plot_line(p1_h, p2_h)
plot_line(p1_v, p2_v)
plt.legend()
plt.show()

# Oppgave b)
def complete_graph(points):
    # Plots alle the lines by looping through each point and plotting the line too the others points
    for i in points:
        for j in points:
            plot_line(i, j)

alfa = np.sqrt(2)/2
points1 = ((0, 0),(1, 0),(0, 1),(1, 1))
points2 = ((1, 0),(alfa, alfa),(0, 1),(-alfa, alfa),(-1, 0),(-alfa, -alfa),(0, -1),(alfa, -alfa))
complete_graph(points1) # Plots the lines in the square
complete_graph(points2) # Plots the lines in the second sequence of points
plt.show()

"""
Terminal > python graph1.py
(Shows two graphs, the other shows after closing the first one)
"""
