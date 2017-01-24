# Prime Number Program
# This program will allow the user to enter a number, then the program will
# determine if this number is a prime number or not. A prime number is the 
# number thats divided by itself and one. Any other numbers that divided to 
# more than one and itself then this numbers is not a prime numbers. for
# example 6 its divided by itself and one, pluse 2,3. so thats not a prime 
# number.

def prime_num ( value ):
    
    if value > 1:
        for num in range ( 2, value):
            if ( value % num ) == 0 or ( value < 1 ):
                return False
            else:
                return True
    else: 
        return False
    
def main():
    
    # ask the user to enter a number to check if its a prime number or not
    # number = int(input('Enter a number : '))
    count1 = 0
    count2 = 0
    for i in range ( 1, 101 ):
        prime = prime_num ( i )
        if prime == True:
            count1 += 1
        else: 
            count2 += 1
            
    print('Prime numbers : ', count1)
    print('Not a prime number : ', count2)
    
main()