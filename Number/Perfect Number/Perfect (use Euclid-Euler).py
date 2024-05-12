import math
# 0 <= n <= 9.10^18
def prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def perfectNum(n):
    for p in range(2, 35):
        if prime(p):
            if prime(2 **p - 1):
                if (2 **(p-1)) * (2 **p-1) == n:
                    return True
    return False

def perfectSequence():
    print('Perfect numbers in the sequence: ', end='')
    for p in range(2, 35):
        if prime(p):
            if prime(2 **p - 1):
                print(f"{(2 **(p-1)) * (2 **p-1)}", end=' ')

if __name__ == '__main__':
    n = int(input('Enter a number: '))
    print(perfectNum(n))
    perfectSequence()
        
        