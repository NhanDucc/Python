n = int(input('Enter length: '))

print('Right-angled triangle: ')
for i in range (0, n):
    for j in range (0, i+1):
        print('*', end = '')
    print()

print()

print('Isosceles right triangle 1: ')
for i in range (0, n):
    for j in range (0, i+1):
        print('*', end = '  ')
    print()

print()

print('Isosceles right triangle 2: ')
for i in range (n, 0, -1):
    for j in range (i, 0, -1):
        print('*', end = '  ')
    print()

print()

print('Isosceles right triangle 3: ')
for i in range (0, n):
    for j in range (0, i):
        print('', end = '  ')
    for j in range (i, n):
        print(' *', end = '')
    print()

print()

print('Isosceles right triangle 4: ')
for i in range (n, 0, -1):
    for j in range (i, 0, -1):
        print('', end = '  ')
    for j in range (i, n):
        print(' *', end = '')
    print()

print()

print('Isosceles triangle 1: ')
for i in range (0, n):
    space = ' ' * (n-i)
    star = '*' * (2*i - 1)
    print(space + star)

print()    

print('Isosceles triangle 2: ')
for i in range (n-1, 0, -1):
    space = ' ' * (n-i)
    star = '*' * (2*i - 1)
    print(space + star)

print()

print('Square: ')
for i in range (n):
    for j in range (n):
        print('*', end = '  ')
    print()   

print()

print('Rectangle: ')
for i in range (n):
    for j in range (n):
        print('*', end = ' ')
    print()   

print()