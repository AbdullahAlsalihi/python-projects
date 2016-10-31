# Book club points 
# This program will ask the user to enter the number of books that
# has been purchased and depend on the total number of books 
# the customer will get some points ex: for each book that has been purchased
# the customer will get 2.5 points for 1 book.

# First: The long way.

# Asking the user to enter the total number of books that has been purchased.
number_of_books = int(input('Please enter number of books purchased: '))

# Declaring points variable for 1 book
points = 2.5

# Declaring variables for total number of books
zero_book = 0
two_book = 2
four_book = 4
six_book = 6
eight_book = 8

# Checking total number of point each customer gets.
if number_of_books == zero_book:
    print('You earned %d points for today purchased.' % (number_of_books * points))
elif number_of_books == two_book:
    print('You earned %d points for today purchased.' % (number_of_books * points))
elif number_of_books == four_book:
    print('You earned %d points for today purchased.' % (number_of_books * points))
elif number_of_books == six_book:
    print('You earned %d points for today purchased.' % (number_of_books * points))
elif number_of_books == eight_book:
    print('You earned %d points for today purchased.' % (number_of_books * points))
else:
    print('Error: Iam sorry I dont have %d in my system.' % (number_of_books * points))
    
# The easiest way: is by taking the the user input and multiplay it with 
# the points variable and then store the result in another variable
# called total and then print the result.....

total = number_of_books * points
print('You earned %d points for today purchased.' % (total))