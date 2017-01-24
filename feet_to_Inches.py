# Feet to Inches Program 
# This program will allow the user to enter the number of feets and 
# the program will calclulated to inches.
# Note: For each Feet There are 12 inches
# Required : Write this program in a function

def feet_to_Inches ( value ):
    inches = 12
    for feet in range( value+1 ):
        total_inches = feet * inches
    return total_inches

def main():
    try:
        # ask the user to enter the number of feet
        feet = int(input( 'Enter the number of feet: ' ))
        inches = feet_to_Inches ( feet )
        print( 'The total inches %d for %d feet' % (inches, feet) )
    except:
        print('ERROR: you didn\'t enter a number.....')
        print('Please enter a number of feet')
    
main()