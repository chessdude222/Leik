import sys
n = int(input())

if n < 4 and n > 1:
    print('NO SOLUTION', file= sys.stdout)

else:
    for low, high in zip(range(int(n / 2) + 1 + n%2, n), range(1, int(n / 2) + n%2)):
        print(high, low, file = sys.stdout, end = ' ')
