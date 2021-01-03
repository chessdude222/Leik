import numpy as np

with open('density.txt', 'r') as infile:
    celsius = []
    density = []
    for line in infile:
        if '#' in line:
            continue
        else:
            values = line.split()
            celsius.append(float(values[0]))
            density.append(float(values[1]))

converter = lambda c: 1.8*c + 32
cel = np.array(celsius)
fahrenheit = converter(cel)

with open('outfile.txt', 'w') as outfile:
    for f_, d_ in zip(fahrenheit, density):
        outfile.write(f'{f_:5.2f} {d_:6.3f}\n')
