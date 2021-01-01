import sys
a = int(input())

for i in range(a):
    y, x = [int(i) for i in input().split()]
    if x > y:
        area = x**2
    else:
        area = y**2

    if area % 2 == 0:
        temp = area - x + 1
        if y < x:
            temp -= (x - y)
    else:
        temp = area - y + 1
        if x < y:
            temp -= (y - x)
    print(temp, file = sys.stdout)
