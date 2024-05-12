import math
import matplotlib.pyplot as plt
import numpy as np
        
class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def get_input(prompt):
        while True:
            value = input(prompt)
            if value.strip() == "":
                print("Invalid input! Please do not leave this field blank.")
            else:
                try:
                    num = int(value)
                    if prompt == "a = " and num == 0:
                        print("There is no quadratic equation because a = 0!")
                    else:
                        return num
                except ValueError:
                    print("Invalid input! Please enter a number.")
    
    def find_root(self):
        delta = self.b * self.b - 4 * self.a * self.c
        if delta != 0:
            if delta > 0:
                return (-self.b + math.sqrt(delta)) / self.a, (-self.b - math.sqrt(delta)) / self.a
            else:
                return None
        else:
            return -self.b / 2
    
    def evaluate(self, x0):
        return self.a * (x0**2) + self.b * x0 + self.c   
    
    def plot(self):
        x = np.linspace(-10, 10, 400)
        y = self.a * x**2 + self.b * x + self.c
        plt.plot(x, y)
        plt.title('Graph of the quadratic equation')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.show()
    
    def __str__(self):
        return f"F(x) = {self.a}x^2 + {self.b}x + {self.c}"

if __name__ == "__main__":
    print("Enter a and b for the quadratic equation:")
    a = Quadratic.get_input("a = ")
    b = Quadratic.get_input("b = ")
    c = Quadratic.get_input("c = ")
    print(Quadratic(a, b, c))

    while True:
        print("Choose an option:")
        print("1. Find the root of the quadratic equation")
        print("2. Evaluate the value of the quadratic equation")
        print("3. Plot the graph of the quadratic equation")
        print("4. Exit")
        option = int(input("Your option: "))
        
        match option:
            case 1:
                root = Quadratic(a, b, c).find_root()
                if root is None:
                    print("The above equation has no root")
                elif isinstance(root, tuple):
                    print(f"The above equation has two distinct roots: {root[0]:.2f} and {root[1]:.2f}")
                else:
                    print(f"The above equation has double root: {root:.2f}")
                break
            
            case 2:
                x0 = Quadratic.get_input("Enter x0 to determine the value of the linear polynomial: ")
                print(f"f({x0}) = {Quadratic(a, b, c).evaluate(x0)}")
                break
            
            case 3:
                Quadratic(a, b, c).plot()
                break
            
            case 4:
                break
            
            case _:
                print("Invalid option!")
                break