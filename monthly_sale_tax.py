# Monthly Sale tax Program 
# A retail company want to file a monthly sale tax for the total sale for a 
# month. The program should calculate then the state and the county sale
# tax collected. The state sale tax rate is 5 percent while the county sale 
# tax is 2.5 Percent.
# Write a program that ask the user to enter the total sale for a month. From 
# that you should figure out the state and the county tax

def state_tax ( value ):
    state_tax_rate = 0.05
    total = 0
    if value < state_tax_rate:
        print( 'This value is less than the state tax rate' )
    else:
        total = state_tax_rate * value
        return total
        
def county_tax ( value ):
    county_tax_rate = 0.025
    total = 0
    if value < county_tax_rate:
        print( 'This value is less than the county tax rate ')
    else:
        total = county_tax_rate * value
        return total

def total_tax ( first , second ):
    total = 0
    total = first + second
    return total

def main():
    tax = int(input('Please enter the monthly income: '))
    state = state_tax ( tax )
    county = county_tax ( tax )
    total = total_tax (state_tax(tax), county_tax(tax))
    print( 'The monthly income for this company is: ', tax )
    print( 'The state tax is : ', state)
    print( 'The county tax is : ', county)
    print( 'The total tax is: ', total)
    
main()
    
        
