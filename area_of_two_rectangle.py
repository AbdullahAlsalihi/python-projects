# The area of rectangle
# asking the user to input the length and the width of the rectangle
# for two rectangles and calculate which one of them have the greater area
# or if they're the same

# First asking the user to enter the length and width of first rectangle
rec1_length = float(input('Enter the length of 1 rectangle: '))
rec1_width = float(input('Enter the width of 1 rectangle: '))
# Second calculating the area of the first rectangle
rec1_area = rec1_length * rec1_width
print('The area of 1 rectangle is: %.2f' % (rec1_area))

print('\n')

# Third asking the user to input the length and width of 2 rectangle
rec2_length = float(input('Enter the length of 2 rectangle: '))
rec2_width = float(input('Enter the width of 2 rectangle: '))
# Fourth calculating the area of 2 rectangle 
rec2_area = rec2_length * rec2_width
print('The area of 2 rectangle is: %.2f' % (rec2_area))

print('\n')

# finding which rectangle have the greatest area

if rec1_area > rec2_area:
    print('Rectangle 1 has the greats area: %.2f' % (rec1_area))
elif rec2_area > rec1_area:
    print('Rectangle 2 has the greats area: %.2f' % (rec2_area))
elif rec2_area == rec1_area:
    print('They are equal......')
