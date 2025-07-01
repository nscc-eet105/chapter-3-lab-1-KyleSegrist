#Kyle_Segrist
#Chapter_3_Lab_1_Workdays
#June_23_2025

print ('Numeric Workday Calculator')
print()
    #get input from the user
choice = "y"
while choice.lower() == "y":
    work_day = int(input( 'Enter the numeric value of the workday you wish to translate: '))

    if work_day < 0 or work_day > 7:
        print ('Invalid Entry, Please enter a value between 0 and 7')
    elif work_day == 0 or work_day > 5:
        print('That workday is a weekend')
    elif work_day == 1:
        print('The workday is Monday')
    elif work_day == 2:
        print('The workday is Tuesday')
    elif work_day == 3:
        print('The workday is Wednesday')
    elif work_day == 4:
        print('The workday is Thursday')
    elif work_day == 5:
        print('The workday is Friday')
    else:
        print ('Invalid Entry, Please enter a value between 0 and 7')

    #See if the user would like to calculate another day
    choice = input('Would you like to calculate another day? (y,n): ')
    print()

print('Goodbye')
