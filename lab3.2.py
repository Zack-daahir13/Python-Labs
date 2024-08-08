import math

x1, y1, = eval(input(" enter point 1 (latitude and longtitude)in degrees: "))
x2, y2, = eval(input(" enter point 2 (latitude and longtitude)in degrees: "))

radius = 6371.01

x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

d = radius * math.acos((math.sin(x1))) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1-y2)
print(" the distance between the two points is", d, "km")