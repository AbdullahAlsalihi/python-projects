# Pennies for pay
# this program will ask the user to enter the number of money for each day
# for how many days. Then double the amount of money in each day.
# display the info in a table form.......

money = int(input('Please enter the amount of money per day: '))
days = int(input('Please enter how many days: '))
cash = 0

print('days \t money')
print('================')
for day in range(days):
    day = day + 1
    cash = (money * day) * 2
    print(day, '\t', cash)

# this is simple output:

'''
days 	 money
================
1 	 2
2 	 4
3 	 6
4 	 8
5 	 10
6 	 12
7 	 14
8 	 16
9 	 18
10 	 20
11 	 22
12 	 24

'''
