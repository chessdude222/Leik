import sys

n = int(input())

if n*(n + 1)/2 % 2 == 1:
    print('NO', file = sys.stdout)

else:
    print('YES', file = sys.stdout)
    print(n//2 + n % 2, file = sys.stdout)
    print(1, 2, end = ' ', file = sys.stdout)
    if n > 3:
        for i in range(4, n + 1, 3):
            print(i, end = ' ', file = sys.stdout)
    print(n//2, file = sys.stdout)
    print(3, end = ' ', file = sys.stdout)
    for n in range(5, n, 3):
        print(n, n + 1, end = ' ', file = sys.stdout)
