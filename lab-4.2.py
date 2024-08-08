import random

# Generate two random integers under 100
num1 = random.randint(0, 99)
num2 = random.randint(0, 99)

# Prompt the user to enter the sum of the two integers
answer = int(input("What is " + str(num1) + " + " + str(num2) + "? "))

# Check whether the answer is correct and report the result
if answer == num1 + num2:
    print("True")
else:
    print("False")