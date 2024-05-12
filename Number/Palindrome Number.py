import math

def palin(n):
    # return str(n) == str(n)[::-1]     # Use string slicing to reverse the number
    rev = 0
    temp = n    # Store the original value because n will be 0 at the end
    while n != 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return temp == rev

if __name__ == '__main__':
    n = int(input('Enter a number: '))
    if palin(n):
        print("Yes")
    else:
        print("No")
