import sys

choice = int(input('1. Calculate the area of a circle:\n2. Calculate the area of a rectangle\n3. Calculate the area of a triangle\n4. Quit'))

if choice == 1:
    radius = int(input('Enter the radius of the circle:'))
    
    area = 3.14159 * (radius * radius)
    
    print(area)

elif choice == 2:
    length = int(input('Enter the length of the rectangle: '))
    
    width = int(input('Enter the width of the rectangle: '))
    
    area = length * width
    
    print(area)
    
elif choice == 3:
    height = int(input('Enter the height of the triangle: '))
    
    width = int(input('Enter the width of the triangle: '))
    
    area = (height * width) / 2
    
    print(area)

elif choice == 4:
    sys.exit()