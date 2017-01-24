# Age specifier program
# This program will ask the user to enter the user age.
# the program will display if the user is infant, child, a teenager
# or an adult

# Asking user age
age = int(input('Please enter your age: '))

# Check the age of the user
if age <= 1:
    print('You\'re infant....')
elif age > 1 and age < 13:
    print('You\'re a child....')
elif age >= 13 and age < 20:
    print('You\'re a teenager....')
elif age >= 20:
    print('You\'re an adult.....')
