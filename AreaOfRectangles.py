width_1 = int(input('Enter the width of your first rectangle: '))
height_1 = int(input('Enter the height of your first rectangle: '))
width_2 = int(input('Enter the width of your second rectangle: '))
height_2 = int(input('Enter the height of your second rectangle: '))

if width_1 < 0 or height_1 < 0 or width_2 < 0 or height_2 < 0:
    print('Your measurements should not be below 0.')
else:
    area_1 = width_1 * height_1
    area_2 = width_2 * height_2
    
if area_1 < area_2:
    print(f'The area of rectangle 1 is {area_1} and the area of rectangle 2 is {area_2}.\nTherefore rectangle 2 is bigger.')

elif area_1 > area_2:
    print(f'The area of rectangle 1 is {area_1} and the area of rectangle 2 is {area_2}.\nTherefore rectangle 1 is bigger.')
