def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return (a * b) // find_gcd(a, b)

if __name__ == '__main__':
    num_1 = int(input('Enter first number: '))
    num_2 = int(input('Enter second number: '))
    
    print("Greatest common divisor of", num_1, "and", num_2, "is", find_gcd(num_1, num_2))
    print("Least common multiple of", num_1, "and", num_2, "is", find_lcm(num_1, num_2))

    # a, b, c = 10, 20, 35
    # print(find_gcd(find_gcd(a, b), c))
