# Print the table headers
print("Kilograms\tPounds\t|\tPounds\tKilograms")
print("---------------------------------------------")

# Print the conversion table entries
for kg in range(1, 11):
    lb = kg * 2.2
    print(kg, "\t\t", format(lb, ".1f"), "\t|\t", end="")
    if kg == 1:
        print(" ", end="")
    print(kg * 10, "\t\t", format((kg * 10) * 0.45, ".2f"))
