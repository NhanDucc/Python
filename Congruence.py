# (a + b) % c = (a % c + b % c) % c
# (a - b) % c = (a % c - b % c) % c
# (a * b) % c = (a % c * b % c) % c
# (a / b) % c = (a % c / b**-1 % c) % c (Modular Multiplicative Inverse)

import math

# n! % (10**9+7)

# n = int(input('Enter a number: '))

# res = 1
# for i in range(1, n+1):
#     res *= i
# print(res % (10**9+7))

# print(math.factorial(n) % (10**9+7))

# res = 1
# for i in range(1, n+1):
#     res *= i
#     res %= (10**9+7)
# print(res)

# a**b % c
a, b, c = map(int, input().split())
res = 1
for i in range(b):
    res *= a
    res %= c
print(res)
