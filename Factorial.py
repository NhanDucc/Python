def calculate_factorical(n):
    if n == 0:
        return 1
    else:
        return n*calculate_factorical(n-1)

n = int(input('Enter the number to calculate the factorial: '))
factorical = calculate_factorical(n)
print(f'{n}! = {factorical}')