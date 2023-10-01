def find_prime_number(n):
    prime_number_list = []
    i = 2
    while i**2 <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_number_list.append(i)
    if n > 1:
        prime_number_list.append(n)
    return prime_number_list

n = int(input('Enter the positive integer to decompose: '))
result = ''
prime_number = find_prime_number(n)
if n <= 0:
    print('Re-enter the positive integer to decompose')
else:
    print(f'{n} = ', end = '')
    for i in range(len(prime_number) - 1):
        print(prime_number[i], end = ' x ')
    print(prime_number[len(prime_number) - 1])