# gcd = greatest common divisor
# scm = smallest common multiple
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return (a * b) / find_gcd(a, b)

num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))

gcd = find_gcd(num_1, num_2)
lcm = find_lcm(num_1, num_2)

print("Greatest common divisor of", num_1, "and", num_2, "is", gcd)
print("Least common multiple of", num_1, "and", num_2, "is", lcm)
