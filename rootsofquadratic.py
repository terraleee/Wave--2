import math
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("This quadratic function has no real roots.")

elif discriminant == 0:
    print("This quadratic function has one real root.")
    root = -b / (2 * a)
    print("The value of the real root is", root)

elif discriminant > 0:
    print("This quadratic function has two real roots.")
    root1 = (-b + math.sqrt(discriminant)) / 2 * a
    root2 = (-b - math.sqrt(discriminant)) / 2 * a
    print("The values of the real roots are", root1, "and", root2)