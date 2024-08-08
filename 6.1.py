def display_increasing_order(num1, num2, num3):
    numbers = [num1, num2, num3]
    sorted_numbers = sorted(numbers)
    print("The numbers in increasing order are:", sorted_numbers)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

display_increasing_order(num1, num2, num3)
