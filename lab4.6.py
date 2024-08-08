x, y, z = eval(input(" enter the three edges: "))

if x + y > z and x + z > y and y + z > x :

    print(" the perimeter is ", x + y + z)

else:

    print(" the input is invalid")