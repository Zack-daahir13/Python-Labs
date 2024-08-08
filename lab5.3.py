print("Miles\tKilometers\t|\tKilometers\tMiles")
print("----------------------------------------------")

for miles in range(1, 21, ):
    kilometers = miles * 1.609
    print(miles, "\t{:.3f}".format(kilometers), "\t|\t", end="")
    for km in range (1, 21,):
        miles = km * 0.621
        if abs(miles - miles) < 0.5:
            print(km, "\t\t{:.3f}".format(miles))
            break
    else:
        print("")
