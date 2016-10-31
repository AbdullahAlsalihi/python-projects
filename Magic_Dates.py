# Ask the user to enter the date of the year
# If the date multiplyed by the month equal the year.
# It means that this date is a magical number for this specific day

# Giving hint for the user
print('Hint :  day = 12 and month = 02 and year = 90')

# Taking the day input
day = int(input('Please enter the date: '))

# Taking the month input
month = int(input('Please enter the month: '))

# Taking the year input
year = int(input('Please enter the year: '))

# check for the magical date
day_month = day * month

# excption handling if the user enter a greater number than it suppose to be
if day > 31:
    print('Error (The range of the day should be btw 1 and 30...)')
if month > 13:
    print('Error (The range of the month should be btw 1 and 12)')
if year > 100:
    print('Error (The range of the year should be btw 00 and 99)')

# Checking the day is magical day or not 
if day_month == year:
    print('Its a magical day: {} / {} / {}'.format(day, month, year))
elif day_month != year:
    print('This day is: {} / {} / {}'.format(day, month, year))