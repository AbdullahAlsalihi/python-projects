# Distance Travel program
# This program calculate the distance of the car by multiplaying the speed 
# by the time. for example distance = speed(40) * time(4)
# create a loop that ilterate to find the distance in each specific time


speed = int(input('Please enter the speed of car in MPH: '))
time_in_hours = int(input('How many hours traveled: '))
distance = 0
hours = 0

print('Hours \t\tDistance Traveled')
print('----------------------------')
for hour in range(time_in_hours):
    hours = hours + 1
    distance = hours * speed
    print(' ' , hours, '\t\t  ', distance)