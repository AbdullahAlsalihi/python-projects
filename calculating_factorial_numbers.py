# Calculating the factorial of a number
# this program will ask the user to enter a number the the program will 
# find the factoral multiplyed number for this factorial.

# for example: 7! = 1x2x3x4x5x6x7 = 5,040

number = int(input('Please enter any number: '))
fac = 1
print('numbers \t factorial')
for factorial in range(1, number+1):
    fac *= factorial
    print('  ' + str(factorial) + '\t\t   ' + str(fac))
    
# simple output for this program will be as following: 

'''
Please enter any number: 3

numbers 	 factorial
  1		   1
  2		   2
  3		   6

'''
