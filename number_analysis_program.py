# number analysis program
# Design a program that allow the user to enter 20 numbers. The program then
# should store the numbers in a list and then display the following data:
#        1. The lowest number in the list
#        2. The highest number in the list
#        3. The total numbers in the list
#        4. The average of numbers in the list

def main() :
    # create an empty list
    num_list = []
    total = 0
    add = 0
    # create a for loop that allow the user to enter 20 numbers and 
    # store them in a list
    for num in range (1, 21):
        print('number %d : ' % (num), end=' ')
        number = int(input())
        num_list.append(number)
        total += 1
        add = sum(num_list)
    print('The list of numbers are: ', end="\n")
    # the lowest number in the list
    lowest = min(num_list)
    print('The lowest number in the list is : ', lowest)
    
    # ther highest number in the list
    highest = max(num_list)
    print('The highest number in the list is : ', highest)
    
    # total number in the list
    print('The total number in the list is : ', total)
    
    # The avarege number for this list is 
    average = total / len(num_list)
    print('The average number in the list is : ', average)
    
    # The sum of the list is 
    print('The sum of the list is : ', add)
main()