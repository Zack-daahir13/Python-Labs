import random

number1 = random.randint(0, 100)
number2 = random.randint(0, 100)

if number1 > number2:
    number1, number2 == number2, number1
answer = eval(input(" what is " + str(number1) + "+" + str(number2) + "?"))
if number1 + number2 == answer:
    print( number1,  "+", number2, "=", answer, "is", "true")
else:
    print(number1, "+", number2, "=", answer, "is", "False ", "the correct answer is", number1 + number2 )
