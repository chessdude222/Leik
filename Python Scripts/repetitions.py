import sys

text = input()
big = 1
s = 1

for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        s += 1
        if s > big:
            big = s
    else:
        s = 1

print(int(big), file = sys.stdout)
