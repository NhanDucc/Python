n = int(input('Enter the number of rows you want to display in the Floyd Triangle: '))
number = 1

for i in range (0, n):
    for j in range (0, i+1):
        print(number, end = ' ')
        number +=1
    print()