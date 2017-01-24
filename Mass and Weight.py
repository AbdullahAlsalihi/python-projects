# Mass and weight calculator
# Ask the user to enter the mass for calculating its weight
# If the object is more than 500 newton display that its 
# too high. If the object is less than 100 display a messege saying that 
# its too low.

# Ask the user to enter the mass
mass = float(input('Please enter the mass of an object: '))

# Creating variable to hold the newton number
newton = 9.8

# Calculate the weight of that object
weight = mass * newton

# Checking if the weight is too high or too low or normal
if weight > 500:
    print('The weight %.1f is too high...' % (weight))
elif weight >= 100 and weight <= 500:
    print('The weight %.1f is normal...' % (weight))
elif weight < 100:
    print('The weight %.1f is too low.....' % (weight))
    
