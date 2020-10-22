from math import factorial, log, e
r = 0
t = 0

for n in range(1, 30):
    t = log(factorial(n))
    r = n*log(n)-n
    print(f"actual:{t: .2f}, stirling:{r: .2f}")
