import math

a, b, c = eval(input("enter the value of a, b, and c :"))

d = pow(b, 2) - 4 * a *  c

if d > 0:
    root1 = ((-b) + math.sqrt((b**2) - 4 * a *  c)) / (2 * a)
    root2 = ((-b) - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    print("the roots are ", round(root1, 6), round(root2, 6))
elif d == 0 :
    root1 = (-b + math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
    print("the roots are ", root1)
else:
    print(" the equation has no real roots")



