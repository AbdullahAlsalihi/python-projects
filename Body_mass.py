# Body mass index program (BMI)
# first we should ask the user to enter the weight and the height 
# the weight in pounds and the height in inches.
# then we will specify what is the BMI for this specific person 
# according to its value output.

weight = int(input('please enter the weight in pounds: '))
height = int(input('Please enter your height in inches: '))

BMI = weight * (703 / (height ** 2))

if BMI >= 18.5 and BMI <= 25:
    print('You consider as optimal with this weight %.2f ' % (BMI))
elif BMI < 18.5:
    print('You consider as underweight with this weight %.2f ' % (BMI))
elif BMI > 25:
    print('You consider as overweight with this weight %.2f ' % (BMI))
else:
    print('You are not a human......')