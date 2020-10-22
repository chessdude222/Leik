import matplotlib.pyplot as plt

def plot(n):
    right = []
    left = []
    for i in range(n):
        plt.plot(n, i, 'go')
        right.append([n, i])
        plt.plot(n+1, i, 'ro')
        left.append([n+1, i])
    for j in right:
        for n in left:
            plt.plot([j[0], n[0]], [j[1], n[1]], 'm')
    plt.show()

plot(2)
