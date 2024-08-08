def display_pattern(n):
    """Displays a pattern of numbers up to n rows."""
    for i in range(1, n + 1):
        # print leading spaces for each row
        print(" " * (2 * (n - i)), end="")

        # print numbers in reverse order
        for j in range(i, 0, -1):
            print("{:2d} ".format(j), end="")

        print()  # print newline at end of row
#  test program that promts user to enter a number line

display_pattern(5)
def display_pattern(n):
    """Displays a pattern of numbers up to n rows."""
    for i in range(1, n + 1):
        # print leading spaces for each row
        print(" " * (2 * (n - i)), end="")
        # print numbers in reverse order
        for j in range(i, 0, -1):
            print("{:2d} ".format(j), end="")

        print()  # print newline at end of row
# prompt user for input
n = int(input("Enter line number: "))
# display pattern
display_pattern(n)