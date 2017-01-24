# Celsius to Fahrenhelt Table
# the program should display a table of celsius to fehrenhelt form the 
# range of 0 to 20. 

celsius = int(input('Please enter celcius tempreture: '))
feh = 0

print('Celsius \tFehrenheit')
print('=========================')
for Cel in range(celsius):
    feh = (9/5) * Cel + 32
    print(' ',Cel , '\t\t', feh)
    
# the output should be like this one:

'''
Celsius 	Fehrenheit
=========================
  0 		 32.0
  1 		 33.8
  2 		 35.6
  3 		 37.4
  4 		 39.2
  5 		 41.0
  6 		 42.8
  7 		 44.6
  8 		 46.4
  9 		 48.2
  10 		 50.0
  11 		 51.8
  12 		 53.6
  13 		 55.400000000000006
  14 		 57.2
  15 		 59.0
  16 		 60.8
  17 		 62.6
  18 		 64.4
  19 		 66.2
'''