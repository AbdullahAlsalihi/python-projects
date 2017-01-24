# This program will ask the user to enter the number of
# attendence people that coming to the cookout and asking 
# how many piece each person will get
# after that the program will calculate the packeges that needs for
# hot dogs and hot dog buns that should be required.

hot_buns = 8
hot_dog = 10
total_sandwiches = 0
minm_hot_dog = 0
minm_hot_bun = 0

attending = int(input('Please enter the number of attending people: '))
pieces = int(input('How many hot dog for each person: '))

total_sandwiches = attending * pieces

minm_hot_dog = total_sandwiches / hot_dog

minm_hot_bun = total_sandwiches / hot_buns

print('Number of people attending the cookout: ')
print('attendece: %d ' % (attending))
print('Pieces: %d' % (pieces))
print('Tottal number of sandwiches: %d' % (total_sandwiches))

integer = 0
hot_dog_left = 0
hot_dog_calc1 = 0
hot_dog_calc2 = 0
hot_dog_buns_left = 0
integers = 0

if type(minm_hot_dog) == float:
    integer = int(minm_hot_dog) + 1
    hot_dog_calc = (integer - minm_hot_dog)
    hot_dog_left = float(format(hot_dog_calc, '.2f')) * 10
    
if type(minm_hot_bun) == float:
    integers = int(minm_hot_bun) + 1
    hot_dog_calc2 = ( integers - minm_hot_bun )
    hot_dog_buns_left = float(format(hot_dog_calc2, '.2f')) * 10
    
print('Min buns packege: %d' % (integers))
print('Min hot dog packege: %d ' % (integer))
print('Hot dogs left : %d ' % (hot_dog_left))
print('Hot buns left : %d ' % (hot_dog_buns_left))
