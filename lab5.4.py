max_num = 0
count = 0

while True:
    num = int(input("Enter an integer (0 to end): "))
    if num == 0:
        break
    if num > max_num:
        max_num = num
        count = 1
    elif num == max_num:
        count += 1

print("The largest number is", max_num)
print("The occurrence count of the largest number is", count)
