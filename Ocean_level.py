# Ocean Level Program 
# this program will calculate the ocean level in one year according to the
# author its 1.6 millimeters per one year, but what if we want to calcultate
# the amount of water in the ocean for 25 years.

rising_water = 1.6
years = 25

print('years \t\t millimeters')

for year in range (1 ,years):
    millimeters = year * rising_water
    print(str(year) + '\t\t' + str(millimeters))