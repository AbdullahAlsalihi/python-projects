# Automobile Cost
# The program should ask the user to enter the monthly cost for the following
# expenses.
#======================
# 1. loan payment
# 2. insurance
# 3. gas
# 4. Oil 
# 5. Tires
# 6. maintanance
#========================

def mounthly_pay(loan, gas, oil, insurance, maitanance):
    total = loan + gas + oil + insurance + maitanance
    return total
    
def annual_cost(cost):
    year_to_months = 12
    total = cost * year_to_months
    return total

def main():
    loan_payment = float(input('Enter the loan payment: '))
    gas = float(input('Enter the gas payment: '))
    oil = float(input('Enter the oil payment: '))
    insurance = float(input('Enter the insurance payment: '))
    maitanance = float(input('Enter the maitanance payment: '))

    monthly_exp = mounthly_pay(loan_payment, gas, oil, insurance, maitanance)
    print('The expenses for this month is: ', monthly_exp)
    
    yearly_exp = annual_cost(monthly_exp)
    print('The expense for this year is: ', yearly_exp)
    
main()