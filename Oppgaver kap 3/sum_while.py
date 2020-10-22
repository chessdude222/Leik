k = 1   # Starting value
M = 3   # Iterations
s = 0   # Sum

while k <= M:
    s += 1/((2*k)**2)
    k += 1

print(f"The sum for M = {M} is {s:.2f}")

"""
Kjøreeksempel:
python sum_while.py
The sum for M = 3 is 0.34
"""
