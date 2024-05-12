import math

def prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input("Enter the first number: "))
    m = int(input("Enter the last number: "))
    prime_list = []
    for i in range(n, m+1):
        if prime(i):
            prime_list.append(i)
        else:
            continue
    print(f"The sequence of prime number from {n} to {m} is: ", end='')
    for i in range(len(prime_list) - 1):
        print(prime_list[i], end = ', ')
    print(prime_list[len(prime_list) - 1])
