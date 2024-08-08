count_pos = count_neg = total = num = 0

while True:
    num = int(input("Enter an integer (0 to quit): "))
    if num == 0:
        break
    elif num > 0:
        count_pos += 1
    else:
        count_neg += 1
    total += num

if count_pos + count_neg == 0:
    print("No numbers were entered.")
else:
    avg = total / (count_pos + count_neg)
    print("The number of positive integers entered is:", count_pos)
    print("The number of negative integers entered is:", count_neg)
    print("The total of the integers entered (not counting zeros) is:", total)
    print("The average of the integers entered (not counting zeros) is: {:.2f}".format(avg))
    