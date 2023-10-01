import math

integer_list = []
n = int(input("Enter the number of element: "))
for i in range(n):
    value = int(input(f"Enter element number {i}: "))
    integer_list.append(value)

prime_number_list = [] 
for i in integer_list:
    if i < 2:
        d = 0
    else:
        d = 1
    for j in range (2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            d = 0 
            break
    if d == 1:
        prime_number_list.append(i)

prime_number_list.sort()        
print(f"The prime numbers are: {prime_number_list}")