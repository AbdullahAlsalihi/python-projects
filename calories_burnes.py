# calories burened
# this program will ask the user to make a for loop that count the time
# form 10 minutes to 30 minutes and multiplay that by the amont of calories
# given as 4.2 for each minute

calories_per_minutes = 4.2
total_calories = 0

for i in range(10, 31, 5):
    total_calories = i * calories_per_minutes
    print('At %d minute the number of calories burned is: %d' \
          % (i , total_calories))
print('The total number of calories burnes in 30 minutes is: ', total_calories)
print('\n')

# creating another version where the user can enter the starting, ending, and
# the number of steps to contoral the loop. and at the same time know the 
# number of calories burnes in a specific time.

start = int(input('Please enter the starting number of minutes: '))
end = int(input('Please enter the ending numebr of minutes: '))
steps = int(input('Please enter the number of steps: '))
print('\n')

for i in range(start, end, steps):
    total_calories = calories_per_minutes * i
    print('At %d minute the number of calories burned is: %d' \
              % (i , total_calories))    
print('The total number of calories burnes in 30 minutes is: ', total_calories)