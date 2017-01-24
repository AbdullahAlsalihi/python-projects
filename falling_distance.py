# Falling Distance Program
# This program will calculate the distance for any object that falling in a 
# specific gravity. There will be a formula that given to you, so that you 
# can use it to calculate the distance which is: d = 1/2 gt^2
# Write a function that accept one argument and then use a loop to go through
# the distance in different amount of time. set the loop to be 10.

from math import pow

def falling_distance ( time ):
    g = 9.8
    d = g * pow(time, 2)
    #print(d)
    for distance in range (1, 10+1 ):
        d = g * ((distance) * pow(time, 2))
        print( '%.2f' % (d) )
        
def main():
    # ask the user to enter the time 
    time = int(input('Enter the time to know the distance: '))
    distance = falling_distance(time)

main()
