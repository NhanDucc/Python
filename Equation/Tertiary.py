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
        delta = self.b **2 - 3*self.a*self.c
        if delta == 0:
            if self.b**3 - 27*a**2*d == 0:
                x = -self.b / (3*self.a)
                return f"The equation has a triple root: {x:.2f}"
            else:
                x = (-self.b + (self.b**3 - 27*a**2*d)**(1/3)) / (3*self.a)
                return f"The equation has only one root: {x:.2f}"
        else:
            k = (9*self.a*self.b*self.c - 2*self.b**3 - 27*self.a**2*self.d) / (2*math.sqrt(abs(delta)**3))
            if delta > 0:
                if abs(k) <= 1:
                    x1 = (2*math.sqrt(delta)*math.cos(math.acos(k)/3) - self.b)/(3*self.a)
                    x2 = (2*math.sqrt(delta)*math.cos(math.acos(k)/3 - 2*math.pi/3) - self.b)/(3*self.a)
                    x3 = (2*math.sqrt(delta)*math.cos(math.acos(k)/3 + 2*math.pi/3) - self.b)/(3*self.a)
                    if x2 == x3 != x1:
                        return f"The equation has simple root: {x1:.2f} and double root: {x2:.2f}"
                    elif x1 == x2 != x3:
                        return f"The equation has simple root: {x3:.2f} and double root: {x1:.2f}"
                    elif x1 == x3 != x2:
                        return f"The equation has simple root: {x2:.2f} and double root: {x1:.2f}"
                    elif x1 != x2 != x3:
                        return f"The equation has three roots: {x1:.2f}, {x2:.2f}, {x3:.2f}"
                else:
                    x = ((math.sqrt(delta)*abs(k))/(3*self.a*k))*((abs(k)+math.sqrt(k**2-1))**(1/3) + (abs(k)-math.sqrt(k**2-1))**(1/3))
                    return f"The equation has only one root: {x:.2f}"
            else:
                x = (math.sqrt(abs(delta))/(3*self.a))*((abs(k)+math.sqrt(k**2-1))**(1/3) + (abs(k)-math.sqrt(k**2-1))**(1/3)) - (self.b/(3*self.a))
                return f"The equation has only one root: {x:.2f}"
    
    def evaluate(self, x0):
        return self.a*(x0 **3) + self.b*(x0 **2) + self.c*x0 + self.d
    
    def plot(self):
        x = np.linspace(-10, 10, 400)
        y = self.a*x**3 + self.b*x**2 + self.c*x + self.d
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
        option = Tertiary.get_input("Your option: ")
        
        match option:
            case 1:
                root = Tertiary(a, b, c, d).find_root()
                print(root)
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
