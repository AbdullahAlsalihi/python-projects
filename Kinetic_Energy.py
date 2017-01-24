# Kinetic Energy Program 
# This program will allow the user to enter the mass and vilocity in order to
# find, Kinetic energy for a specific object. In order to calculate that, 
# you need the following formula : KE = 1/2 mv^2
# Return the kinetic energy result in a function.

from math import pow

def kinetic_Energy ( mass, vilocity ):
        
    KE = 1/2 * (mass * pow(vilocity, 2))
    return KE

def main():
    # ask the user to enter the mass
    mass = int(input('Enter the mass : '))
    # ask the user to enter the vilocity 
    vilocity = int(input('Enter the vilocity: '))
    
    Ke = kinetic_Energy ( mass, vilocity )
    print( 'The kinetic energy for this object is : ', Ke ) 
    
main()