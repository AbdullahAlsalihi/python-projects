# Future Value Program
# this program will allow the user to determine the amount of saving 
# that she/ he will suppose to have, if they wanna do some saving. 
# the formula given as : F = P * ( 1 + i ) ^ t

from math import pow

def future_value ( p, i , t ):
    F = p * (( 1 + i ) ** t)
    return F

def main():
    p = int(input('Enter the present value: '))
    i = float(input( 'Enter the intreset : '))
    t = int(input('Enter the number of months : '))
    
    value = future_value ( p, i , t )
    print('The future value : %.2f'% ( value ))
    
main()