# create a program that ask the user to enter a number. 
# this number should be less than 100. If the number is greater than 
# 100 it will raise exception handling by telling the user that this 
# number is greater than 100. else print the multiplyed number

# create a variable called number to store the user input
number = int(input('Please enter a number: '))

# create a condition controlled loop that checks if the number is less than 
# 100. If True, multiply the number by 10 and print the result. After that ask
# the user agian to enter another number, if this number is less than 100 do 
# the same task, else print an error messege
while number < 100:
    product = number * 10
    print(product)
    number = int(input('Enter another number: '))

# Thats the error messege if the user enter greater than 100
print('Error: this number is greater than 100.')
print('Try agian......')
    