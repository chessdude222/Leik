import sys
n = int(input())

def algo(n):
    values = []
    while n != 1:
        values.append(int(n))
        if n % 2 == 0:
            n /=2
        else:
            n = 3*n + 1
    values.append(1)
    return values

list = algo(n)
for i in list:
    print(i, file = sys.stdout, end = ' ')
