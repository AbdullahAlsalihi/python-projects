# Math Quiz Program
# This program will do a simple math quizzes. The number should pick up 
# randomly and then displayed in this following:
#          456
#         +
#          476
#        ========
# The program should allow the student to enter the answer. If the answer was
# correct, then the program will display Congrandulation you guest it. 
# Otherwise, the program should display that this answer is wrong and gave 
# them the correct answer.

import random

def main ():
    
    first_num = random.randint(1, 1000)
    second_num = random.randint(1, 1000)

    print( '\t', first_num, '\t', first_num, '\t', first_num, '\t', first_num)
    print( '\t', '+', '\t', '-', '\t', '*', '\t', '/' )
    print( '\t',second_num,'\t',second_num, '\t', second_num,'\t', second_num)
    print( '\t', '====', '\t', '====', '\t', '====', '\t', '====')
    
    try:
        number = int(input('\nEnter a number for summation ( + ): '))
        summation = first_num + second_num
        if number == summation:
            print( 'Congradulation YOU Guest the summation', summation )
        else:
        
            print( 'This answer is wrong for (+) .....', number )
            print( 'The correct answer is', summation )
    except:
        print( 'This answer is wrong for (+) .....', number )
        print( 'The correct answer is', summation )        

    try:
        number = int(input('\nEnter a number for substraction ( - ): '))
        substract = first_num - second_num
        if number == substract:
            print( 'Congradulation YOU Guest the substraction', substract )
            
        else: 
            print( 'This answer is wrong for (-).....', number )
            print( 'The correct answer is', substract )               
    except:
                    
        print( 'This answer is wrong for (-).....', number )
        print( 'The correct answer is', substract )    
        
    try:
        number = int(input('\nEnter a number for multiplay ( * ): '))
        multiplay = first_num * second_num
        if number == multiplay:
            print( 'Congradulation YOU Guest the multiplay', multiplay )
            
        else:
            print( 'This answer is wrong for (*) .....', number )
            print( 'The correct answer is', multiplay )            
    except:
                            
        print( 'This answer is wrong for (*) .....', number )
        print( 'The correct answer is', multiplay )  
            
    try:
        number = int(input('\nEnter a number for divid ( / ): '))
        divid = first_num / second_num
        if number == divid:
            print( 'Congradulation YOU Guest the divid', divid )
        else: 
            print( 'This answer is wrong for ( / ).....', number )
            print( 'The correct answer is', divid )             
    except:
                                        
        print( 'This answer is wrong for ( / ).....', number )
        print( 'The correct answer is', divid )      
main()