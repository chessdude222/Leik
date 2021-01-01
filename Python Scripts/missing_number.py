import sys

a = int(input()); b = input().split()
original = a*(a+1)/2
list = sum([float(i) for i in b])

print(int(original - list), file = sys.stdout)
