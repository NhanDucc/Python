C = int(input('Enter the temperature in degrees C: '))
if 0 <= C <= 10**5:
    F = (C*9/5) + 32
    print('%.2f' %F)
else:
    print('Please re-enter the temperature in degrees C')
