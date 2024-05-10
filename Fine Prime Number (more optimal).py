import math

def prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    num_list = []
    n = int(input('Enter the number of elements:'))
    for i in range(n):
        value = int(input(f'Enter the value {i+1}:'))
        num_list.append(value)
    
    prime_list = []
    for i in num_list:
        if prime(i):
            prime_list.append(i)
        else:
            continue
    prime_list.sort()
    print(prime_list)
