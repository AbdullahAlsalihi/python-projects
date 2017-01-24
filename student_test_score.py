# student grades_average
# this program will ask the user to enter the number of students and
# how many test scores each one gets according to specific number of test
# the user will enter both (student numbers and test scores) the program 
# then will dispaly the average score for each specific student according 
# to their test scores.

students = int(input('Please enter how many students: '))
test_score = int(input('how many test for each one: '))

for student in range(students):
    print('student num ', student + 1, ' : ')
    print('==============')
    total = 0
    for num_score in range(test_score):
        print('score num ', num_score + 1, end= " ")
        score = float(input(' : '))
        total += score


    average = total / test_score

    print('student number ', student + 1 , ' : ', average , ' average score.')