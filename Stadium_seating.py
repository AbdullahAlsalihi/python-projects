# Stadium Seating Program
# This program is clasify into three catigories: 
#        1. Class A : 20 $ for seat
#        2. Class B : 15 $ for seat
#        3. Class C : 10 $ for seat
# This program will display the amount of tickets that have beem sold for 
# each class and the total amount of seats for every class and the total
# amount of income that have been generated from the ticket sale



# this function will calculate the cost income for the people who bought 
# class A ticket which worth 20 dollars. 
# this will allow the user to ente the amount of ticket sold for this 
# specific class and calculate the income for this specific categories

def class_A ( value ):
    seat = 20
    total = 0
    for ticket in range(value):
        total += seat
    return total

# this function will calculate the cost income for the people who bought 
# class B ticket which worth 15 dollars. 
# this will allow the user to ente the amount of ticket sold for this 
# specific class and calculate the income for this specific categories

def class_B ( value ):
    seat = 15
    total = 0
    for ticket in range(value):
        total += seat
    return total

# this function will calculate the cost income for the people who bought 
# class C ticket which worth 10 dollars. 
# this will allow the user to ente the amount of ticket sold for this 
# specific class and calculate the income for this specific categories

def class_C ( value ):
    seat = 10
    total = 0
    for ticket in range(value):
        total += seat
    return total

def main():
    # Hint : 
    print('\n')
    print(' Please select one of the following:  ')
    print('     1. Class A : press A')
    print('     1. Class B : press B')
    print('     1. Class C : press C')
    print('     1. display income : press total')
    print('\n')
    # ask the user to enter the seat categories A, B, C
    user_input = input('Please enter seat categories: ')
    if user_input == 'A':
        # ask the user to enter the number of tickets sold
        ticket_sold = int(input('Enter the number of tickets for A : '))
        A_class = print('Class A tickets income: ',class_A (ticket_sold))
    elif user_input == 'B':
        # ask the user to enter the number of tickets sold
        ticket_sold = int(input('Enter the number of tickets for B : '))
        B_class = print('Class B tickets income: ',class_B (ticket_sold))
    elif user_input == 'C':
        # ask the user to enter the number of tickets sold
        ticket_sold = int(input('Enter the number of tickets for C : '))
        C_class = print('Class C tickets income: ' ,class_C (ticket_sold))
    elif user_input == 'total':
        # ask the user to enter the number of tickets sold
        ticket_sold1 = int(input('Enter the number of tickets for A : '))
        ticket_sold2 = int(input('Enter the number of tickets for B : '))
        ticket_sold3 = int(input('Enter the number of tickets for C : '))
        A_class = class_A (ticket_sold1)
        B_class = class_B (ticket_sold2)
        C_class = class_C (ticket_sold3)
        total = (A_class + B_class + C_class)
        print('The amount of income generated for ticket sale is : ', total)
main()