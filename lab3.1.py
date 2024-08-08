import math

length = eval(input(" enter the length from the center to a vertex: "))

s = 2 * length * math.sin(math.pi/5)

area = 3 * math.sqrt(3)/ 2 * pow(s, 2)

print(" area of pentagon is ", area)