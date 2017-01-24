# Time calculater program
# this program will ask the user to enter the number of seconds 
# then it will convert the number of seconds to how many minutes, hours 
# and days according to the number of seconds that the user input.

# then create an if statment saying that if the number of seconds that
# the user input is 60 or greater than that then display the number of 
# minutes and seconds

# then create another if statment saying that if the number of seconds is 
# 3600 it means one hours, and its greater than 3600. then display the number 
# of hours, minutes and seconds according to user input

# the last if statment will be if the user input 86400 seconds that for one 
# day, or greater than this number. then display the number of days, hours ,
# minutes and seconds according to user input.

# I added another one just for fun. If the user input 31536000 thats for one
# year or greater than this number. then the program should display the number
# of years, days, hours, minutes and seconds. According to user input.

number_of_seconds = int(input('Please enter the number of seconds: '))

one_minute = 60
one_hour = 3600
one_day = 86400
one_year = 31536000


if number_of_seconds < one_hour:
    minutes = number_of_seconds // one_minute
    seconds = number_of_seconds % one_minute
    print(str(minutes) + ' minutes.', str(seconds) + ' seconds')

    
elif number_of_seconds < one_day:
    hours = number_of_seconds // one_hour
    find_seconds = number_of_seconds % one_hour
    minutes = find_seconds // one_minute
    seconds = find_seconds % one_minute
    print(str(hours) + ' hours', str(minutes) + ' min', \
          str(seconds) + ' seconds')

elif number_of_seconds < one_year:
    days = number_of_seconds // one_day
    find_hours = number_of_seconds % one_day
    hours = find_hours // one_hour
    minutes = (find_hours // one_minute)% one_minute
    seconds = find_hours % one_minute
    print(str(days) + ' days' , str(hours) + ' hours', str(minutes) + ' min', \
              str(seconds) + ' seconds')   

elif number_of_seconds >= one_year:
    years = number_of_seconds // one_year
    find_years = number_of_seconds % one_year
    days = find_years // one_day
    hours = (find_years // one_hour) % 24
    minutes = (find_years // one_minute) % one_minute
    seconds = find_years % one_minute
    print(str(years) + ' year' , str(days) + ' days' , str(hours) + ' hours', \
          str(minutes) + ' min', str(seconds) + ' seconds')    
    
    

