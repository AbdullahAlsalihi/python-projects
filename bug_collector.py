# bug collector program
# this program will find the total number of bugs collected in five days 
# the program should ask the user to enter the number of bugs collected in 
# every specific day and add the number to the total.
# at the end the program should display the total number of bugs that have been
# collected in this specific time.

# declar a variable that holds the total number of bugs that been collected
total_number_of_bugs = 0

# declar a variable for the amount of days 
days = 5

# declar a for loop that ilterate 5 times and asking the user how many bugs 
# has been collected in this specific day and at the end count the total number
# of bugs.
for day in range(days):
    bug_collector = int(input('number of bugs: '))
    print('number of bugs in', day + 1, 'day is: ', bug_collector )
    total_number_of_bugs += bug_collector
print('Total number of bugs collected in %d days is : %d bugs' \
      % (days , total_number_of_bugs))