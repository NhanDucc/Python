# gcd = greatest common divisor
# scm = smallest common multiple
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_scm(a, b):
    gcd = find_gcd(a, b)
    scm = (a * b) // gcd
    return scm

num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))

gcd = find_gcd(num_1, num_2)
scm = find_scm(num_1, num_2)

print("Greatest common divisor of", num_1, "and", num_2, "is", gcd)
print("Smallest common multiple of", num_1, "and", num_2, "is", scm)