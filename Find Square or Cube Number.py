import math

def square_number(n):
    result = math.isqrt(n)
    return result * result == n

def cube_number(n):
    result = int(math.pow(n, 1/3))
    return (result ** 3 == n) or ((result + 1) ** 3 == n)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if square_number(n):
        print(f"{n} is a square number.")
    elif cube_number(n):
        print(f"{n} is a cube number.")
    else:
        print(f"{n} is neither a square number nor a cube number.")
