import math

def combination(n, k):      # math.comb(n, k)
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

if __name__ == '__main__':
    n = int(input('Enter n: '))
    k = int(input('Enter k: '))
    print(f'Number of ways to choose {k} items from {n} items without repetition and without order is {combination(n, k)}')
