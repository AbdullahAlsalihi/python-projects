# Budget calculater
# this program will ask the user to enter the number of budget for this 
# month and then ask them agian what they bought in this month and at the 
# end count the total of purchases that they made and tell the user if they 
# are under or over the budget.

budget_per_month = int(input('Please enter the budget for this month: '))
purchaseses = int(input('Who many purchases did you made: '))
total = 0
money_left = 0

for i in range(purchaseses):
    items = input('Place name: ')
    money = int(input('Who much did you spend: '))
    print(i + 1, ':', items, '. Money spend: ', money )
    total += money
if total > budget_per_month:
    print('The total purchases %d is over your budget %d .' \
          % (total, budget_per_month ))
else:
    money_left = budget_per_month - total
    print('The total purchases %d is under your budget %d.' \
             'you still have %d' % (total, budget_per_month, money_left))
    
    
    
    