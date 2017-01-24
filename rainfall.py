# Rain fall program 
# This program will let the user to enter the total rain fall for 12 months
# in to a list. Then the program should calculate the total rain fall for
# a year, the average monthly rainfall and the months that have the higher 
# and lower amounts.

def main() :
    num_list = []
    total = 0
    
    for i in range (1, 5):
        print('Enter the rainfall for %d month :'%(i), end=" ")
        rainfall = float(input())
        num_list.append(rainfall)
        
    for num in num_list:
        total += num
        
    ave = total / len(num_list)
    
    print('Total rainfall for a year : %.2f' % (total))
    print('The average is : %.2f' % (ave))
    
    maxi = max(num_list)
    mini = min(num_list)
    
    print('The maximum rainfall for a year is : ', maxi)
    print('The minimum rainfall for a year is : ', mini)
    
main()