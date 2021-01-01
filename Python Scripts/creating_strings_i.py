from itertools import permutations
from math import factorial
import sys

string = input()
list = sorted(set(["".join(p) for p in permutations(string)]))

print(len(list), file = sys.stdout)

for i in list:
    print(i, file = sys.stdout)
