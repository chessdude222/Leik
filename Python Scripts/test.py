from itertools import permutations
from math import factorial
import sys

string = input()
"""
dict = {i:string.count(i) for i in string}
string.sort(reverse = False)
string = ''.join(string)
"""
list = sorted(set(["".join(p) for p in permutations(string)]))


print(len(list), file = sys.stdout)

for i in list:
    print(i)
    if i == None:
        pass
    #else:
        #print("".join(i), file = sys.stdout)
