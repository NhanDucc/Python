n = int(input('Enter the number to convert to decimal system: '))
base = 10

decimal_number_list = []
while n > 0:
    decimal_number = n % base
    decimal_number_list.append(decimal_number)
    n = n // base
decimal_number_list.reverse()

result = ''
for i, decimal_number in enumerate(decimal_number_list):
    result += f'{decimal_number}*{base}^{len(decimal_number_list)-i-1} + '
result = result.rstrip(' + ')
print(result)