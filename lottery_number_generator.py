# Lottery Number Generator
# Design a program that generates a seven digit lottery number. The program
# should generate a seven random numbers between 0 to 9, and assign each 
# number to a list element. Create another loop that display the content of 
# the list.

import random

def main():
    numbers = 7
    digit = 0
    num_list = []
    
    for num in range(numbers):
        digit = random.randint(0,9)
        num_list.append(digit)
        
    print('The list element: ',num_list)
    
    for i in num_list:
        print('. ' ,i, ' .')

main()