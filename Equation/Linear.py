import matplotlib.pyplot as plt
import numpy as np

class Linear:
    def __init__(self, a, b):
        if a == 0:
            print("The value of a cannot be zero")
            quit()
        self.a = a
        self.b = b
    
    def get_input(prompt):
        while True:
            value = input(prompt)
            if value.strip() == "":
                print("Invalid input! Please do not leave this field blank.")
            else:
                try:
                    num = int(value)
                    if prompt == "a = " and num == 0:
                        print("There is no Linear equation because a = 0!")
                    else:
                        return num
                except ValueError:
                    print("Invalid input! Please enter a number.")
    
    def find_root(self):
        return -self.b / self.a
    
    def evaluate(self, x0):
        return self.a * x0 + self.b
    
    def plot(self):
        x = np.linspace(-10, 10, 400)
        y = self.a * x + self.b
        plt.plot(x, y)
        plt.title('Graph of the linear equation')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.show()
    
    def __str__(self):
        return f"F(x) = {self.a}x + {self.b}"

if __name__ == "__main__":
    print("Enter a, b, c and d for the Linear equation:")
    a = Linear.get_input("a = ")
    b = Linear.get_input("b = ")
    print(Linear(a, b))

    while True:
        print("Choose an option:")
        print("1. Find the root of the linear equation")
        print("2. Evaluate the value of the linear equation")
        print("3. Plot the graph of the linear equation")
        print("4. Exit")
        option = int(input("Your option: "))
        
        match option:
            case 1:
                root = Linear(a, b).find_root()
                print(f"The above equation has one root: {root:.2f}")
                break
            
            case 2:
                x0 = int(input("Enter the value of x: "))
                print(f"The value of the above equation at x = {x0} is {Linear(a, b).evaluate(x0)}")
                break
            
            case 3:
                Linear(a, b).plot()
                break
            
            case 4:
                break
            
            case _:
                print("Invalid option!")
                break