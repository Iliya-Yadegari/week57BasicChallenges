weight_input = int(input('Enter your weight in pounds: '))
height_input = int(input('Enter your height in inches'))

bmi = weight_input * 703 / (height_input * height_input)

if bmi > 25:
    print('Overweight')
elif bmi < 18.5:
    print('Underweight')
elif bmi > 18.5 and bmi < 25:
    print('Optimal weight')