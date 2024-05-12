import math

def perfectNum(n):
    sum = 1
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            sum += i
            if i != n // i:
                sum += n // i
    return sum == n

if __name__ == '__main__':
    n = int(input('Enter a number: '))
    print(perfectNum(n))
        
# When n is too large, the program will run for a long time!