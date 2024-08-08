# Prompt the user to enter the weight and price of each package of rice
w1, p1 = map(float, input("Enter weight and price of package 1: ").split())
w2, p2 = map(float, input("Enter weight and price of package 2: ").split())

# Calculate the cost per unit for each package and compare
if p1/w1 < p2/w2:
    print("Package 1 has the better price.")
elif p1/w1 > p2/w2:
    print("Package 2 has the better price.")
else:
    print("The two packages have the same price.")