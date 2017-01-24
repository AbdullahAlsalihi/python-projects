# nested loop program 
# this program will make a tree upside down by creating two nested loops
# this loop will start from the top to buttom for example it will start by
# printing 8 ********* and then 7 and so on till it reach 1

for i in range(8, 0, -1):
    for j in range(i):
        print('#' , end = '')
        
    print()

# That what the output should be:
    
'''
########
#######
######
#####
####
###
##
#
'''