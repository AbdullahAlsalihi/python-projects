# Population Program 
# This program will predict the approximate size of population of organism. 
# the program will ask the user to enter the satring number of organizm and 
# the average daily increase by percentage and lastly the number of days to 
# multiply

# First taking the user input
number_organizm = int(input('Starting number of organizms: '))
average_daily_increase = int(input('Average daily increase: '))
days_multiply = int(input('Number of days multiply: '))

# second converting the percentag to decemal by dividing by 100
converting_percentage = average_daily_increase / 100


print('the Approximate size of population in Day 1 is %d' % (number_organizm))
print('The table below show the rest each day: ')
print('Day Approximate \t Population')

# Third creating a for loop that goes through the days and then take the 
# starting number of organizm and multiply it by the converting percentage
# and then add the total to the starting number of organizm, now the new 
# value became the the starting number for the next day, multiply it by the 
# converting percentage and add the total to the past result of organizm and 
# so own untill the loop finished.

for day_approximate in range(2, days_multiply+1):
    number_organizm = (number_organizm * converting_percentage) +\
        number_organizm
    
    print('   ' + str(day_approximate) + '\t\t\t    ' + str(number_organizm))