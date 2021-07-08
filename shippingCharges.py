weight = int(input('Enter the weight of the package: '))
distance = int(input('Enter the distance the package will travel: '))


if weight > 20 or weight < 0:
    print('Invalid weight!')

if distance < 10 or distance > 3000:
    print('Invalid distance!')
    
distance_t = distance % 500

distance_i = (distance - distance_t) / 500

if weight <= 2:
    money = distance_i * 1.1
    print(money)

elif weight > 2 and weight <= 6:
    money = distance_i * 2.2
    print(money)

elif weight > 6 and weight <= 10:
    money = distance_i * 3.7
    print(money)

elif weight > 10 and weight <= 20:
    money = distance_i * 4.8
    print(money)    