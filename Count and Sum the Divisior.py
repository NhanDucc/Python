import math

def count_divisior(n):
    count = 0
    for i in range(1, math.isqrt(n)+1): 
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

def sum_divisor(n):
    sum = 0
    for i in range(1, math.isqrt(n)+1): 
        if n % i == 0:
            sum += i
            if i != n // i:
                sum += n // i
    return sum

if __name__ == "__main__":
    n = int(input('Enter a number: '))
    print('Number of divisors:', count_divisior(n))
    print('Sum of divisors:', sum_divisor(n))
