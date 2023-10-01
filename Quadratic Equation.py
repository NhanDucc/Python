import math

print("Enter the base a, b and c of the quadratic equation")
a = int(input("Enter the base a: "))
b = int(input("Enter the base b: "))
c = int(input("Enter the base c: "))
delta = b*b - 4*a*c

if a == 0:
    print("There is no quadratic equation because a = 0!")
else:
    print(f"Quandratic equation: {a}x^2 + {b}x + {c} = 0")
    if delta != 0:
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / a
            x2 = (-b - math.sqrt(delta)) / a
            print(f"The above equation has two distinct roots: {x1:.2f} and {x2:.2f}")
        else:
            print("The above equation has no root")
    else:
        x = -b / 2
        print(f"The above equation has double root: {x:.2f}")