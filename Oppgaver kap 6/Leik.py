def plot_line1(p1, p2):
    plt.plot(p1[0], p1[1], 'go', label = 'p1')    # Plots the points
    plt.plot(p2[0], p2[1], 'ro', label = 'p2')
    if p2[0] - p1[0] != 0:
        a = (p2[1] - p1[1])/(p2[0] - p1[0])
        f = lambda x: a*x - p1[0]*a + p1[1]
        x = np.linspace(p1[0], p2[0], 300)
        y = f(x)
    else:
        x = np.array([p2[0]]*300)
        y = np.linspace(p1[1], p2[1], 300)
    plt.plot(x, y, 'm', label = 'line')
