import random

def printMatrix(n):
    """Prints an n-by-n matrix with random 0's and 1's."""
    for i in range(n):
        for j in range(n):
            print(random.randint(0, 1), end=" ")
        print()  # print newline at end of row


# prompt user for input
n = int(input("Enter n : "))

# display matrix
printMatrix(n)
