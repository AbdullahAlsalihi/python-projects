# Total sale program 
# This program will ask the user to enter the sales for a specific store
# for each day in a week. The amounts should be sorted in a list and calculate
# the total sale for the week, and the average.

def main():
    # ask the user to enter the store sales for one week
    
    week = 7
    week_sale = [0] * week
    total = 0.0
    
    for weeks in range(week):
        print('Enter the sales for day %d : '% (weeks+1), end= " ")
        week_sale[weeks] = float(input())
        
    for num in week_sale:
        total += num

    print('Total sale for this week : %.2f' % (total))
    
main()