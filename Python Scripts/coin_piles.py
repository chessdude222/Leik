import sys
a = int(input())


for i in range(a):
    right, left = [int(i) for i in input().split()]
    if max(right, left) > min(right,left)*2:
        print('NO', file = sys.stdout)
    elif (right + left) % 3 == 0:
        print('YES', file = sys.stdout)
    else:
        print('NO', file = sys.stdout)
