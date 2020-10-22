# Makes two lists to contain weight and natural abundance
m_i = []
w_i = []

with open('oxygen.txt', 'r') as infile:
    infile.readline() # Skips the first line
    for line in infile:
        # Adds values too the two lists containing weight and natural abundance
        values = line.split()
        m_i.append(float(values[1]))
        w_i.append(float(values[2]))


s = 0                       # Set the sum to zero
for n in range(len(m_i)):
    # Sums up all the values by looping trough the two lists
    s += m_i[n]*w_i[n]

print(f"The molar mass of oxygen is {s:.4f} g/mol")

"""
Terminal > python read_file_isotopes.py
The molar mass of oxygen is 15.9994 g/mol
"""
