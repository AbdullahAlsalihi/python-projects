# shiping charges
# The fast freight fishing company ask you to right 
# a program that calculate the amount of weight for each specific
# packege and each packege has a different weight depending on the 
# user and how much money they wont to spend
# each weight has a different price.

weight_amount = int(input('please enter the amount of weight: '))
price = 0
if weight_amount <= 2:
    price = weight_amount * 1.50
    print('the price for this weight is: 1.50 $')
    print('Your total will be: %.2f' % (price))
elif weight_amount > 2 and weight_amount <= 6:
    price = weight_amount * 3.00
    print('the price for this weight is: 3.00 $')
    print('Your total will be: %.2f' % (price)) 
elif weight_amount > 6 and weight_amount <= 10:
    price = weight_amount * 4.00
    print('the price for this weight is: 4.00 $')
    print('Your total will be: %.2f' % (price))  
elif weight_amount > 10:
    price = weight_amount * 4.75
    print('the price for this weight is: 4.75 $')
    print('Your total will be: %.2f' % (price))  
else:
    print('This weight is invaild. Purchase another one. Thx')