# Colored Mixed program 
# This program will ask the user to enter the color and then check
# if the color is one of the three primary colors(red, green, blue)
# then find the mixed color, if not then it will output an Error message


# Asking the user to enter to colors
color1 = input('Please enter the first color: ')
color2 = input('Please enter the second color: ')

red = 'red'
blue = 'blue'
yellow = 'yellow'

if color1 == red and color2 == blue:
    print('%s color and %s color have mixed of Purple' % (color1, color2))
    
elif color1 == blue and color2 == red:
    print('%s color and %s color have mixed of Purple' % (color1, color2))
    
elif color1 == yellow and color2 == red:
    print('%s color and %s color have mixed of Orange' % (color1, color2))
    
elif color1 == red and color2 == yellow:
    print('%s color and %s color have mixed of Orange' % (color1, color2))
    
elif color1 == blue and color2 == yellow:
    print('%s color and %s color have mixed of Green' % (color1, color2))
    
elif color1 == yellow and color2 == blue:
    print('%s color and %s color have mixed of Green' % (color1, color2))
    
else: 
    print('Error there are color that are not a primary color')