# write a program that ask the user to enter the name of the file. then 
# the program will display the contant of the file, with numbers in front of
# them. for every line that been readed you should put a comma.

file_name = input('Enter the file name: ')
file = open(file_name, 'r')
count = 0
for line in file:
    line = line.rstrip('\n')
    count += 1
    print(count, line, end = ', ')