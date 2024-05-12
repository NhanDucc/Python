# Chưa phân biệt được nghiệm bội và nghiệm duy nhất
# Chưa tính được khi delta = 0
# 2 nghiệm


import math
import matplotlib.pyplot as plt
import numpy as np

class Tertiary:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def get_input(prompt):
        while True:
            value = input(prompt)
            if value.strip() == "":
                print("Invalid input! Please do not leave this field blank.")
            else:
                try:
                    num = int(value)
                    if prompt == "a = " and num == 0:
                        print("There is no tertiary equation because a = 0!")
                    else:
                        return num
                except ValueError:
                    print("Invalid input! Please enter a number.")
    
    def find_root(self):
        delta = self.b **2 - 3 * self.a * self.c
        k = (9 * self.a * self.b * self.c - 2 * self.b **3 - 27 * self.a **2 * self.d) / (2 * math.sqrt(abs(delta) **3))
        if delta != 0:
            if delta > 0:
                if abs(k) <= 1:
                    return (2 * math.sqrt(delta) * math.cos(math.acos(k) / 3) - self.b) / (3 * self.a), (2 * math.sqrt(delta) * math.cos(math.acos(k) / 3 - (2 * math.pi) / 3) - self.b) / (3 * self.a), (2 * math.sqrt(delta) * math.cos(math.acos(k) / 3 + (2 * math.pi) / 3) - self.b) / (3 * self.a)
                else:
                    return (math.sqrt(delta) * abs(k)) / (3 * self.a * k) * ((abs(k) + math.sqrt(k **2 - 1)) **(1 / 3) + (abs(k) - math.sqrt(k **2 - 1)) **(1 / 3)) - self.b / (3 * self.a)
            else:
                return ((math.sqrt(abs(delta))) / (3 * self.a)) * ((abs(k) + math.sqrt(k ** 2 - 1)) **(1 / 3) + (abs(k) - math.sqrt(k **2 - 1)) **(1 / 3)) - self.b / (3 * self.a)
        else:
            return (-self.b + (self.b ** 3 - 27 * self.a ** 2 * self.d) ** (1 / 3)) / (3 * self.a)
    
    def evaluate(self, x0):
        return self.a * (x0 **3) + self.b * (x0 **2) + self.c * x0 + self.d
    
    def plot(self):
        x = np.linspace(-10, 10, 400)
        y = self.a * x**3 + self.b * x**2 + self.c * x + self.d
        plt.plot(x, y)
        plt.title('Graph of the tertiary equation')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.show()
    
    def __str__(self):
        return f"F(x) = {self.a}x^3 + {self.b}x^2 + {self.c}x + {self.d}"
if __name__ == "__main__":
    print("Enter a, b, c and d for the tertiary equation:")
    a = Tertiary.get_input("a = ")
    b = Tertiary.get_input("b = ")
    c = Tertiary.get_input("c = ")
    d = Tertiary.get_input("d = ")
    print(Tertiary(a, b, c, d))

    while True:
        print("Choose an option:")
        print("1. Find the root of the tertiary equation")
        print("2. Evaluate the value of the tertiary equation")
        print("3. Plot the graph of the tertiary equation")
        print("4. Exit")
        option = int(input("Your option: "))
        
        match option:
            case 1:
                root = Tertiary(a, b, c, d).find_root()
                if root is None:
                    print("The above equation has no real root!")
                elif isinstance(root, tuple):
                    if len(root) == 3:
                        print(f"The above equation has three roots: {root[0]:.2f}, {root[1]:.2f}, {root[2]:.2f}")
                    elif len(root) == 2:
                        print(f"The above equation has two roots: {root[0]:.2f}, {root[1]:.2f}")
                else:
                    print(f"The above equation has one root: {root:.2f}")
                break
            
            case 2:
                x0 = int(input("Enter the value of x: "))
                print(f"The value of the above equation at x = {x0} is {Tertiary(a, b, c, d).evaluate(x0)}")
                break
            
            case 3:
                Tertiary(a, b, c, d).plot()
                break
            
            case 4:
                break
            
            case _:
                print("Invalid option!")
                break