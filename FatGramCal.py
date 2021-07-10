import sys

calories = int(input("Enter number of calories: "))
fats = int(input("Enter number of fat in grams: "))

if(calories > 0 and fats > 0):
   cf = fats * 9
   
else:
    print('The calories or/and the fats cannot be below 0 try again')
    sys.exit()

if(cf < calories):
       percent = cf / calories  
else:
    print("Error input. Calories from fat cannot more than total calories")
    sys.exit()

if(percent < 0.3):
    print("Food is low in fat")