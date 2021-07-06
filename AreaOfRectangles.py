import sys

try:
    width1 = int(input("Enter the width of the first rectangle: "))
    height1 = int(input("Enter the height of the first rectangle: "))
    width2 = int(input("Enter the width of the second rectangle: "))
    height2 = int(input("Enter the height of the second rectangle" ))
except:
    print("You should enter only numbers!!!")
    sys.exit()

area1 = width1 * height1
area2 = width2 * height2

print("Area of the first rectangle is", area1)
print("Area of the second rectangle is", area2)

if area1 > area2:
    print("The first rectangle is bigger")
elif area1 < area2:
    print("The second rectangle is bigger")
else:
    print("Rectangles are equal")