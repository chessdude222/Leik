from math import factorial

n = 14
k = 3
sum_1 = 1


for j in range(1,(n-k+1)):
    print(j)
    sum_1 = sum_1*((k+j)/j)

binomial = factorial(n)/(factorial(k)*factorial(n-k))

print(binomial)
print(sum_1)
