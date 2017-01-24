# Kilometer Converter Program
# This program will ask the user to enter the distence in kilometer
# the program then will display the distance in miles.

# The miles function will calculate the convertion from kilometer
# to miles.
def miles(distance):
    converter = distance * 0.6214
    return converter
# Take the user input for kilometer and display the result.
kilometer = int(input('Please enter the amount of KM to convert: '))
print('The distance in Kilometer is : %d' % (kilometer))
print('The distance converted to miles is : %.2f' % (miles(kilometer)))
