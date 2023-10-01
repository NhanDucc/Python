import math

Fibonacci_list = []
n = int(input('Number of first Fibonacci numbers: '))

for i in range (1, n+1):
    Fibo = round(((1 + math.sqrt(5))**i - (1 - math.sqrt(5))**i)/(2**i * math.sqrt(5)))
    Fibonacci_list.append(Fibo)

print(f'{n} first Fibonacci numbers:', end = ' ')
for i in range(len(Fibonacci_list) - 1):
   print(Fibonacci_list[i], end = ', ')
print(Fibonacci_list[len(Fibonacci_list) - 1])