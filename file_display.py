# Create a text file name number.txt and store random numbers and store it 
# in the desktop. Then create a program that allow the user to pol up 
# the numbers form the text file to the compiler.

file = open('numbers.txt', 'r')
find = file.readline()

while find != "" :
    find = find.rstrip('\n')
    print(find)
    find = file.readline()
    
file.close()