# Rock, Paper, scissors Game Program
# This program will allow the user to play agianst the computer, first, the 
# program will randomly generate a random number from 1 to 3 : 1 for rock, 
# 2 for paper, and 3 for scissors. then the choice will store tell the 
# user enter the choice after that the computer display the random choice.

import random

def game ( choice ):
    # create a random number generater
    number = random.randrange (1,4)
    # create an if statment
    if number == 1:
        print ( 'Computer choice : Rock' )
    elif number == 2:
        print( 'Computer choice : Paper' )
    else:
        print ( 'Computer choice : Scissors' )
        
    if number == 1 and choice == 3 or choice == 1 and number == 3:
        print ( 'The rock smashes the scissors..' )
    elif number == 3 and choice == 2 or choice == 3 and number == 2:
        print ( 'The Scissor cut paper...' )
    elif number == 1 and choice == 2 or choice == 1 and number == 2:
        print ( 'The paper ate the rock...' )
    elif number == 1 and choice == 1:
        print ( 'its equal, play one more time ' )
    elif number == 2 and choice == 2:
        print ( 'its equal, play one more time ' )
    elif number == 3 and choice == 3:
        print ( 'its equal, play one more time ' )
    else:
        print('Play agian')

def main ():
    # ask the user to enter a choice 
    rock = 1
    paper = 2
    scissor = 3
    
    print('\nrock = 1')
    print('paper = 2')
    print('scissors = 3\n')
    
    choice = int(input('enter your choice from the following: '))
    comp = game (choice)
    
    
main()