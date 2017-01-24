# Roman numbers specifier..
# Asking the user to input number from 1 to 10
# and then specify which roman letter it should be  
# If the user enter a number more than 10 it will display an error messege.

# Asking the user to enter a number btw range 1 to 10
numbers = int(input('Please enter numbers from 1 to 10: '))

# Specifying variable for each number 

one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9
ten = 10

# Checking which number related to another roman numerals
# if the user enter a number not in the range of 1 to 10 
# it will display an error messege......

if numbers == one:
    print('The number %d is I in Roman Numerals.' % (numbers))
elif numbers == two:
    print('The number %d is II in Roman Numerals.' % (numbers))
elif numbers == three:
    print('The number %d is III in Roman Numerals.' % (numbers))
elif numbers == four:
    print('The number %d is IV in Roman Numerals.' % (numbers))
elif numbers == five:
    print('The number %d is V in Roman Numerals.' % (numbers))
elif numbers == six:
    print('The number %d is VI in Roman Numerals.' % (numbers))
elif numbers == seven:
    print('The number %d is VII in Roman Numerals.' % (numbers))
elif numbers == eight:
    print('The number %d is VIII in Roman Numerals.' % (numbers))
elif numbers == nine:
    print('The number %d is IX in Roman Numerals.' % (numbers))
elif numbers == ten:
    print('The number %d is X in Roman Numerals.' % (numbers))
else:
    print('The number %d is not btw the range 1 to 10' % (numbers))
    print('Please try agian.......')