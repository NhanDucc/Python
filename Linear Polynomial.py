# Xây dựng lớp đa thức bậc nhất để thể hiện các đa thức bật nhất có dạng:

# F(x)= ax+b (a luôn khác 0)

# Xây dựng các phương thức: (3 điểm)
# a. Phương thức cho phép xác định giá trị của đa thức ứng với x=xo (tính F(xo) )
# b. Phương thức trả về nghiệm đa thức bậc 1 (nghĩa là F(x)=0)
# c. Phép toán cộng (operator +) để cộng hai đa thức bậc nhất

class Linear_Polynomial:
    def __init__(self, a, b):
        if a == 0:
            print("The value of a cannot be zero")
            quit()
        self.a = a
        self.b = b
    
    def evaluate(self, x0):
        return self.a * x0 + self.b
    
    def find_root(self):
        return -self.b / self.a
    
    def __add__(self, other):
        if isinstance(other, Linear_Polynomial) :
            a_new = self.a + other.a
            b_new = self.b + other.b
            return Linear_Polynomial(a_new, b_new)
        else:
            print("Only two linear polynomials can be added")
    
    def __str__(self):
        return f"{self.a}x + {self.b}"

# a
print("Enter a and b for the first linear polynomial:")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
poly_1 = Linear_Polynomial(a, b)


x0 = int(input("Enter x0 to determine the value of the linear polynomial: "))
result =poly_1.evaluate(x0)
print(f"f({x0}) = {result}")

print()

# b
root = poly_1.find_root()
print(f"The root of f(x) = {a}x + {b} is: x = {root}")

print()

# c
print("Enter a and b for the second linear polynomial:")
a_new = int(input("Enter a: "))
b_new = int(input("Enter b: "))
poly_2 = Linear_Polynomial(a_new, b_new)
poly_sum = poly_1 + poly_2

print()

print(f"The sum of two linear polynomial is: {poly_sum}")
