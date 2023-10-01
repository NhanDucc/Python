import math

n = int(input("Enter the first number: "))
m = int(input("Enter the last number: "))
prime_list = []

for i in range(n, m + 1):
    if i < 2:
        d = 0
    else:
        d = 1
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            d = 0
            break
    if d == 1:
        prime_list.append(i)
        
print(f"The sequence of prime number is: {prime_list}")