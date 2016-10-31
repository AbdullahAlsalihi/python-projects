# Roulette wheel colors
# On this program the roulette wheel are numbered from 0 to 36
# for each specific number there are refeard to a specific color.

# Ask the user to enter a number from the range of 0 to 36

numbers = int(input('Please enter a number btw 0 to 36 : '))

# checking each level and its color

if numbers == 0:
    print('Its green....')
elif numbers >= 1 and numbers <= 10:
    if numbers % 2 == 0:
        print('Its even. Its black....')
    else:
        print('Its red.....')
elif numbers >= 11 and numbers <= 18:
    if numbers % 2 == 0:
        print('Its even. Its red.....')
    else:
        print('Its black.....')
elif numbers >= 19 and numbers <= 28:
    if numbers % 2 == 0:
        print('Its even. Its black.')
    else:
        print('Its red.....')
elif numbers >= 29 and numbers <= 36:
    if numbers % 2 == 0:
        print('Its even. Its red.......')
    else:
        print('Its black.....')
        
else:
    print('Error: This is out of range.')
    print('Please try agian.......')