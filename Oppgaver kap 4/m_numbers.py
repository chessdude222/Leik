
def m_num(n):
    sum = 0
    L = [int(i) for i in str(n)]
    for r in range(len(L)):
        sum += (int(L[r]))**(int(L[r]))
    if sum == n:
        return n
    else:
        return f"{n} is not a munchausen number"

numbers = []
for i in range(1, 100000):
    if i == m_num(i):
        numbers.append(i)
    else:
        pass

print(numbers)
