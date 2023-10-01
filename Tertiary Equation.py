import math

print("Enter the base a, b, c and d of the tertiary equation")
a = int(input("Enter the base a: "))
b = int(input("Enter the base b: "))
c = int(input("Enter the base c: "))
d = int(input("Enter the base d: "))

delta = b*b - 3*a*c
k = (9*a*b*c - 2*b**3 - 27*a**2*d)/(2*math.sqrt(abs(delta)**3))

if a == 0:
    print("There is no tertiary equation because a = 0!")
else:
    print(f"Tertiary equation: {a}x^3 + {b}x^2 + {c}x + {d} = 0")
    if delta != 0:
        if delta > 0:
            if abs(k) <= 1:
                x1 = (2*math.sqrt(delta)*math.cos(math.acos(k)/3) - b)/(3*a)
                x2 = (2*math.sqrt(delta)*math.cos(math.acos(k)/3 - (2*math.pi)/3) - b)/(3*a)
                x3 = (2*math.sqrt(delta)*math.cos(math.acos(k)/3 + (2*math.pi)/3) - b)/(3*a)
                print(f'The above equation has three distinct roots: {x1:.2f}, {x2:.2f} and {x3:.2f}')
            else:
                x = (math.sqrt(delta)*abs(k))/(3*a*k)*((abs(k) + math.sqrt(k**2 - 1))**(1/3) + (abs(k) - math.sqrt(k**2 - 1))**(1/3)) - b/(3*a)
                print(f'The above equation has only one root: {x:.2f}')
        else:
            x = ((math.sqrt(abs(delta)))/(3*a))*((abs(k) + math.sqrt(k**2 - 1))**(1/3) + (abs(k) - math.sqrt(k**2 - 1))**(1/3)) - b/(3*a)
            print(f'The above equation has only one root: {x:.2f}')
    else:
        x = (-b + (b**3 - 27*a**2*d)**(1/3))/(3*a)      
        print(f'The above equation has triple root: {x:.2f}')