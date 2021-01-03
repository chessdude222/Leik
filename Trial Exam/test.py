from math import ceil, floor

def is_symmetrical(num):
    num = str(num)
    print(num[:len(num)//2+1], num[len(num)//2:])
    return num[:len(num)//2+len(num)%2] == num[len(num)//2:][::-1]

print(is_symmetrical(1))
