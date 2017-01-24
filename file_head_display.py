# Write a program that ask the user to ente the name of any file and if its 
# found, the program then should display the first 5 numbers. If the file 
# contain numbers less than 5 numbers it should display the hole contant.

search = input('Please enter file name: ')
file = open(search, 'r')
#find = file.readline()

#while find != "" :
    #find = find.rstrip('\n')
    #print(find)
    #find = file.readline()
  
for line in file:
    num = int(line)
    if num == 7:
        break
    print(num)