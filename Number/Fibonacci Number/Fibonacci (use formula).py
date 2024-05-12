import math

# Print the Fibonacci sequence of n numbers
Fibonacci_list = []
n = int(input('Number of first Fibonacci numbers: '))

for i in range (0, n):
    Fibo = round(((1 + math.sqrt(5))**i - (1 - math.sqrt(5))**i)/(2**i * math.sqrt(5)))
    Fibonacci_list.append(Fibo)

print(f'{n} first Fibonacci numbers:', end = ' ')
for i in range(len(Fibonacci_list) - 1):
   print(Fibonacci_list[i], end = ', ')
print(Fibonacci_list[len(Fibonacci_list) - 1])

# Find the nth Fibonacci number (starting from 0)
n = int(input('Enter the ordinal number of the Fibonacci number to find: '))
fibo = round(((1 + math.sqrt(5))**n - (1 - math.sqrt(5))**n)/(2**n * math.sqrt(5)))

print(f'Fibonacci number {n} is: {fibo}')