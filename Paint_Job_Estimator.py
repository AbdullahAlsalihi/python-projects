# Paint Job Estimater Program
# This program will allow the user to enter the squar foot for the space 
# that should be painted and determaine, how many hours of labors and 
# the paint gallons required.
# The company charges 35 $ per hour for labor.
#         1. For every 112 ft of wall space, 1 gallon of paint and 8 hours 
#            of labor will be required. 
#         2. The program should display the following
#            1. The number of gallons of paint required
#            2. The hours of labor required
#            3. The cost of the paint
#            4. The labor charges
#            5. The total cost of the paint job

def gallons ( value ):
    square_feet = 112
    result = 0
    laber_hours = 8
    total = 0
    hours = 1
    charges = 1
    # ask the user for the cost of paint that required 
    paint_cost = int(input('Please enter the cost of paint: '))    
    for i in range(1 , value, square_feet):
        total += 1
        hours = total * laber_hours
        charges = hours * 35
        result = charges + paint_cost
    print('the number of gallons required is ', format(total, ',.2f'))
    print('The total number of hours required is : ', hours) 
    print('The labor charges is : ', charges)
    print('The total cost of paint is: ', result)
    
def main():
    # ask the user to enter the square feet of a wall space 
    wall_space = int(input('Please enter the square feet of a wall: '))
    display = gallons(wall_space)
    
main()
    

       
        
        
