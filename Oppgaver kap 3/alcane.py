M_c = 12.011    # g/mol, molar mass of carbon
M_h = 1.0079    # g/mol, molar mass of hydrogen

start = 2       # Starting value for n
stop = 9        # Last value for n

while start <= stop:
    m = 2*start + 2 # Hydrogen atoms
    mass = m*M_h + start*M_c
    print(f"M(C{start}H{m}) = {mass:3.3f} g/mol")
    start += 1

"""
Kjøreeksempel
python alcane.py
M(C2H6) = 30.069 g/mol
M(C3H8) = 44.096 g/mol
M(C4H10) = 58.123 g/mol
M(C5H12) = 72.150 g/mol
M(C6H14) = 86.177 g/mol
M(C7H16) = 100.203 g/mol
M(C8H18) = 114.230 g/mol
M(C9H20) = 128.257 g/mol
"""
