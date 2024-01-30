import math
n = int(input("Enter the number of values: "))
list = []
for i in range (1, n+1):
    value = int(input(f"Enter value {i}: "))
    list.append(value)

S = 0
for i in list:
    S += i
M = S / n
print(f"Mean: {M}")

S1 = 0
for i in list:
    S1 = sum((i - M)**2 for i in list)
    # x = i - M
    # x = x*x
    # S1 += x
Sd = math.sqrt((1/(n-1))*S1)
print(f"Standard deviation: {Sd}")
