# Prompt the user to enter the number of minutes
minutes = int(input("Enter the number of minutes: "))

# Calculate the number of years and days for the given number of minutes
minutes_per_year = 365 * 24 * 60
years = minutes // minutes_per_year
days = (minutes % minutes_per_year) // (24 * 60)

# Display the result
print(minutes, "minutes is approximately", years, "years and", days, "days.")