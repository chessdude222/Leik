import numpy as np
import matplotlib.pyplot as plt

def filereader(filename):
    with open(filename, 'r') as infile:
        n = len(infile.readlines())     # Checks how many lines in the document

    with open(filename, 'r') as infile:
        delta_x = np.zeros(n)           # Creates the arrays that will be filled with values
        abs_error = np.zeros(n)
        n_values = np.zeros(n)
        master = []
        for line in infile:
            values = line.split(',')        # Splits the lines so you can read the values by indexing
            for i in range(len(values)):    # Checks all the elements in values, and takes away everything that is not a number
                for p in values[i]:
                    if p.isdigit():
                        values[i] = values[i][values[i].index(p):]
                        break
                master.append(values[i])    # Makes all the values go into one list

        for j in range(len(master)): # Strips all the numbers, and converts them to floats
            master[j] = master[j].strip()
            master[j] = float(master[j])
        print(master)
        for l in range(0,len(master), 6): # Loops through the list of values and fills the arrays
                delta_x[int(l/6)] = master[l]
                abs_error[int(l/6)] = master[l+3]
                n_values[int(l/6)] = master[l+5]

    return delta_x, abs_error, n_values

delta_x, abs_error, n_values = filereader('derivative.txt')     # Makes the arrays we the then plot
plt.semilogy(n_values, delta_x, 'g', label = 'delta x')
plt.semilogy(n_values, abs_error, 'r', label = 'absolute error')
plt.xlabel('n-values')
plt.legend()
plt.show()

"""
The absolute error increases because the closer we get to value we are trying to
approximate, the more innacurate your approximation becomes
"""

"""
Terminal > plot_round_off_error.py
(shows a graph)
"""
