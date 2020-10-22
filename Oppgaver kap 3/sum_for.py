s = 0   # sum
M = 3   # iterations

# Range function needed to start from 1, and needed to add 1 to M to finish with the right k value
# The parenthesis for 2k^2 were wrong
# The value that changed in the for function were wrong, and didn't do anything

for k in range (1,(M+1)):
    s += 1/((2*k)**2)

print(f"The sum for M = {M} is {s:.2f}")

"""
Kjøreeksempel:
python sum_for.py
The sum for M = 3 is 0.34
"""
