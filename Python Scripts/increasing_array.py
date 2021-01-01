import sys
a = input(); numbers = [int(i) for i in input().split()]
turns = 0

for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        turns += int(numbers[i] - numbers[i + 1])
        numbers[i + 1] = (numbers[i] - numbers[i + 1]) + numbers[i + 1]


print(turns, file = sys.stdout)
