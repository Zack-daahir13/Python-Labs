import math

# Prompt the user to enter the number of sides and their length
n = int(input("Enter the number of sides: "))
s = float(input("Enter the length of a side: "))

# Calculate the area of the regular polygon using the formula
area = (n * s**2) / (4 * math.tan(math.pi / n))

# Display the result
print("The area of the regular polygon is:", area)