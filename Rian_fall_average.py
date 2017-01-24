# Rain Fall program average
# this program will calculate the number of rainfall for a specific amount
# of years. then the program will ilterate 12 times for each year and at the 
# same time ask for the number of inches for this specific month.

# ask the user for number of years
years = int(input('Please enter the number of years: '))
num_years = 0
num_months = 0
months = 12
average = 0
total = 0

for year in range(years):
    num_years = year + 1
    for month in range(months):
        num_months = month + 1
        inches = int(input('Please enter the number of inches: '))
        total += inches
        print(num_years, 'year\t\t' , num_months, 'month\t\t', inches,'inches')
    average = total / months
    print('\nThe average rainfall for %d year is : %d\n' \
          % (num_years, average))