P = 1000 # initial amount
n = 3 # years
r = 5 # interest rate in %
A = P*(1+r/100)**n # money after n years

print(f"After {n} years {P} euros has grown to{A: g}")

"""
Kjøreeksempel:
python interest_rate.py
After 3 years 1000 euros has grown to 1157.63
"""
