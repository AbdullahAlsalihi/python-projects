# write a program that ask the user for the actual value for a piece of
# property and display the assesment value and the property tax.
# HINTE:
# If the property value is 10000 $$ then we will deduct 60 % of the actual
# price and then the price will be after the deduction is 6000 $$. They take
# 72 cents for each 100 $$ for the accesment value. So the tax for the acre
# assessed at 6000 $$ will be 43.20


def assessment_value (value):
    tax = 0.6 # this is the discount for the appartment
    assess_value = int((value * tax) + 1)# this will hold the assessment value
    #total = assess_value / 100
    #acre = (total * 72) / 100
    total = 0 # storing the total
    # This loop will count every 100 and store it as 72....
    for i in range(1, assess_value, 100):
        i = 72 # this will hold the assessment value for each 100 store 72 ...
        total += i # this will hold the total assessment value
    return (total/100) # return the total value 
        
def main():
    # asking the user to enter the actual price
    actual_price = int(input('Please enter a price: '))
    print(assessment_value(actual_price))
    
main()