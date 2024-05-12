import math

def separate_to_prime(n):
    prime_list = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: # i is prime
            while n % i == 0:
                prime_list.append(i)
                n //= i
    if n > 1: # n is prime
        prime_list.append(n)
    return prime_list
        
if __name__ == "__main__":
    n = int(input('Enter a number: '))
    if n < 2:
        print('Invalid input')
        exit()
    for i in range(len(separate_to_prime(n))-1):
        print(separate_to_prime(n)[i], end='*')
    print(separate_to_prime(n)[-1])