# Money Counting Game
# Create a program that will take the user input
# from pennies, nickels, dimes, and quarters and then add the total
# if the total equal to 1 dollar then the program should congradulate
# the user for making a dollar and at the sametime tell him if its 
# more or less

pennies = int(input('Number of Pennies: '))
nickels = int(input('Number of nickels: '))
dimes = int(input('Number of Dimes: '))
quarters = int(input('Number of quarters: '))

total = pennies + nickels + dimes + quarters

money = total / 100

if money == 1:
    print('Congratulation..... You make a dollar :' , money)
elif money < 1:
    print('Thats less than a dollar.............')
    print('The amount of money: %.2f  Its less than a dollar.' % (money))
elif money > 1:
    print('Thats more than a dollar.......')
    print('The amount of money: %.2f  Its more than a dollar.' % (money))
    