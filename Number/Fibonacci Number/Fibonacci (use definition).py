def fiboSequence(n):    # Print the Fibonacci sequence of n numbers
    if n <= 0:
        print('Invalid input')
    elif n == 1:
        print('0')
    elif n == 2:
        print('0 1')
    else:
        print('0 1', end=' ')
        f1, f2 = 0, 1
        for i in range(2, n):
            fn = f1 + f2
            print(fn, end=' ')
            f1, f2 = f2, fn

def checkFibo(n):   # Check if n is a Fibonacci number
    if n == 0 or n == 1:
        return True
    f1, f2 = 0, 1
    for i in range(2, 101):     # Usually, we don't check for Fibonacci numbers that are too large
        fn = f1 + f2
        if fn == n:
            return True
        f1, f2 = f2, fn
    return False

def findFibo(n):    # Find the nth Fibonacci number
    if n == 0 or n == 1:
        return n
    f1, f2 = 0, 1
    for i in range(2, n+1):
        fn = f1 + f2
        f1, f2 = f2, fn
    return fn

if __name__ == '__main__':
    fiboSequence(10)
    print(checkFibo(13))
    print(findFibo(13))