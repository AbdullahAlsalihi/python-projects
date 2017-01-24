# Sum Of Numbers program
# this program will ask the user to enter a series of positive numbers and 
# then find the total number
# If the user entered a negative number the program should quit and give the
# last total of positive numbers



total = 0
while True:
    
    number = int(input('Please enter a number: '))
    if number > 0:
        total += number
        print('Counting total numbers: %d' % (total))
    else:
        print('\nYour entered a negative number.')
        print('Last counting total was: ', total)
        break
    

        