calories = int(input("Enter number of calories: "))
fats = int(input("Enter number of fat in grams: "))
if(calories > 0 and fats > 0):
   cf = fats * 9
   if(cf < calories):
       percent = cf / calories  
       if(percent < 0.3):
           print("Food is low in fat")
   else:
       print("Error input. Calories from fat cannot more than total calories")
else:
   print("Error input. Calories and fats must be more than 0")
   