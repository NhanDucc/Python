def calculate_factorical(n):        # math.factorial
    if n == 0:
        return 1
    else:
        return n*calculate_factorical(n-1)

n = int(input('Enter the number to calculate the factorial: '))
print(f'{n}! = {calculate_factorical(n)}')