# Converts from Celsius to Fahrenheit
def celsiusToFahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

# Converts from Fahrenheit to Celsius
def fahrenheitToCelsius(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return celsius

# Test program to display the conversion tables
print("Celsius\tFahrenheit\t|\tFahrenheit\tCelsius")
print("-" * 45)

for celsius in range(40, 30, -1):
    fahrenheit = celsiusToFahrenheit(celsius)
    print(celsius,"\t", format(fahrenheit, ".1f"), "\t\t|\t", end="")
    fahrenheit = 110 - (celsius - 30) * 10
    celsius = fahrenheitToCelsius(fahrenheit)
    print(format(fahrenheit, ".1f"), "\t\t", format(celsius, ".1f"))
    