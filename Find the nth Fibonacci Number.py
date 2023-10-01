import math

n = int(input('Enter the ordinal number of the Fibonacci number to find: '))
fibo = round(((1 + math.sqrt(5))**n - (1 - math.sqrt(5))**n)/(2**n * math.sqrt(5)))

print(f'Fibonacci number {n} is: {fibo}')