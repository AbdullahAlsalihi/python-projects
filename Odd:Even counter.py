# Odd/Even Counter
# This program will determine or count, how many odd and even numbers. The 
# program shouldn't ask the user to enter any numebr, you should use a 
# random moduel that will generat 100 numbers, then the program will determin
# if its odd or even and at the same time count the total for both of them.

import random

def main():
    # create a for loop that will loop 100 times and generate 100 random 
    # numbers. After that use an if statment to determine if the random 
    # number is odd or even.
    
    count_even = 0 # variable to hold the even numbers
    count_odd = 0 # variable to hold the odd numbers
    
    for num in range (1, 101):
        
        random_num = random.randrange(1, 200)
        
        if random_num % 2 == 0:
            
            count_even += 1
            
        else:
            
            count_odd += 1
            
    print( 'The odd numbers : ', count_odd )
    print( 'The even numbers : ', count_even )
        
main()