# Day of the week program 
# Asking the user to enter a number btw 1 and 7.
# Each number will corspond to a specific day form the week 

number_of_days = int(input('Please enter any number btw 1 and 7:'))
# Creating variables that can hold the user input numbers
Mon = 1
Tue = 2
Wed = 3 
Thu = 4
Fri = 5
Sat = 6
Sun = 7
# Checking user input and testing it if its related to any of the week days.
# At the end if the user entered another number than the 7th it will handle it
if number_of_days == Mon:
    print('Its Monday...')
elif number_of_days == Tue:
    print('Its Tuesday...')
elif number_of_days == Wed:
    print('Its Wednsday...')
elif number_of_days == Thu:
    print('Its Thursday...')
elif number_of_days == Fri:
    print('Its Friday...')
elif number_of_days == Sat:
    print('Its Saturday...')
elif number_of_days == Sun:
    print('Its Sunday....')
else:
    print('There are no other numbers other than these for the week.')