# Calories from Fate and Carbohydrates.
# This program will allow the user to enter the number of grams. Then the 
# program will calcaulate the calories from fat and the calories from the
# carbohydrates. This program will benefit the people who wanna do diet, for
# letting them know the amount of calories and carbohydrates they lost in 
# one specific day.

def Calories ( grams ):
    # the fat contian 9 calories per gram
    cal_gram = 9
    # this will calculate the calories per gram
    calories_fat = grams * cal_gram
    return ( calories_fat)
def carbohydrates ( grams ):
    # the carbohydrates contain 4 calories per gram
    car_gram = 4
    # this will calculate the carbohydrates per gram
    calories_carbs = grams * car_gram
    return (calories_carbs)
def main():
    # allowing the user to enter the grams for calculating the calories and
    # the carbohydrates that the user has.......
    calories = int(input('Please enter the fat in grams: '))
    print('The calories from fat is :', Calories(calories))
    print('The calories from carbohydrate is : ', carbohydrates(calories))
    
main()