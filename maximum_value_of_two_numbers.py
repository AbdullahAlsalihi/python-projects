# Maximum Of Two Values Program
# This program will allow the user to enter two values, then the program will
# identify which of of the two values are the greatest than the other.
# for example: If the user enter 7 for the first value
#              And 8 for the second value.
#      . Then the program will display a message saying that, number 8 
#        (Which is the second value) is the greates.

def maximum (value_one, value_two):
    if value_one > value_two:
        return value_one
    else:
        return value_two
    
def main():
    # ask the user to enter the first value
    first_value = int(input('enter the first value: '))
    # ask the user to enter the second value
    second_value = int(input('enter the second value: '))
    # storing the result in a variable called maxi
    maxi = maximum (first_value, second_value)
    # printing the maximum value of the two numbers
    print('The maximun value is : ', maxi)
    
    
main()
    