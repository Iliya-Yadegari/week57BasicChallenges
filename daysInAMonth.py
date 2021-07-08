year = int(input('Enter the year: '))

month = int(input('Enter the month: '))

if month > 12 or month < 1:
    print('Your entered an invalid number try again.')

else:
    if year % 4 == 0:
        if month == 2:
            print('No of days: 29')
    
    elif year % 4 != 0:
        if month == 2:
             print('No of days: 30')
    
    if month == 1 or month == 5 or month == 8 or month == 10 or month == 12 or month == 3 or month == 7:
            print('No of days: 31')
    elif month == 4 or month == 11 or month == 6 or month == 10 or month == 9:
        print('no of days: 30')