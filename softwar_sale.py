# Softwar Sale program 
# In this program we will ask the user to enter the number of
# packeges that has been purchased and then found out the total
# and the percentage that related to the amount that has been purchased 
# for this specific visit. After that find out the total amount of money 
# that the customer should pay for this visit.

print('')
packeges = int(input('Please enter the number of packeges for today: '))
one_packege = 99

if packeges >= 10 and packeges <= 19:
    purchased_money = packeges * one_packege
    discount = (purchased_money * 10) / 100
    final_price = purchased_money - discount
    
    print('\n(o)The actual price for this purchas is: %d'%(purchased_money))
    print('(o)Because you bought ', \
          '%d packeges you will get 10 percent discount.' % (packeges))
    print('(o)You bought %d you will get %.2f$ discount'%(packeges, discount))
    print('(o)Befor the price of the item was: %.2f $' % (purchased_money))
    print('(o)Now the new price is: %.2f $ \n' % (final_price))

elif packeges >= 20 and packeges <= 49:
    purchased_money = packeges * one_packege
    discount = (purchased_money * 20) / 100
    final_price = purchased_money - discount
    
    print('\n(o)The actual price for this purchas is: %d'%(purchased_money))
    print('(o)Because you bought ', \
          '%d packeges you will get 20 percent discount.' % (packeges))
    print('(o)You bought %d you will get %.2f$ discount'%(packeges, discount))
    print('(o)Befor the price of the item was: %.2f $' % (purchased_money))
    print('(o)Now the new price is: %.2f $ \n' % (final_price))  
    
elif packeges >= 50 and packeges <= 99:
    purchased_money = packeges * one_packege
    discount = (purchased_money * 30) / 100
    final_price = purchased_money - discount
        
    print('\n(o)The actual price for this purchas is: %d'%(purchased_money))
    print('(o)Because you bought ', \
          '%d packeges you will get 30 percent discount.' % (packeges))
    print('(o)You bought %d you will get %.2f$ discount'%(packeges, discount))
    print('(o)Befor the price of the item was: %.2f $' % (purchased_money))
    print('(o)Now the new price is: %.2f $ \n' % (final_price))      
    
elif packeges >= 100:
    purchased_money = packeges * one_packege
    discount = (purchased_money * 40) / 100
    final_price = purchased_money - discount
            
    print('\n(o)The actual price for this purchas is: %d'%(purchased_money))
    print('(o)Because you bought ', \
          '%d packeges you will get 40 percent discount.' % (packeges))
    print('(o)You bought %d you will get %.2f$ discount'%(packeges, discount))
    print('(o)Befor the price of the item was: %.2f $' % (purchased_money))
    print('(o)Now the new price is: %.2f $ \n' % (final_price))  
    
else:
    purchased_money = packeges * one_packege
    print('\n(o)There is no discounts applied to your purchase today.')
    print('(o)Your purchase did not reach the amount of packeges that')
    print('(o)required you to get any discount. Sorry\n')
    print('(o)Your purchase today will be: %.2f $$'% (purchased_money))
    print('(o)The actual price for this purchas is: %.2f$$'%(purchased_money))