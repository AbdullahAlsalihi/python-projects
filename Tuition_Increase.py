# Tuition Increase
# There is a college that cost for attending any student is 8000 $$
# they announced that the tuition will increase by 3 % each year for the
# next five years. 

full_time_tuition = 8000
years = 5
percent = 0.03

print('years: \t Tuition Increased by: \t Tuition:')

for tuition in range(1, years+1):
    increasedTuition = percent * tuition
    money_spend = increasedTuition * full_time_tuition
    print(' ' + str(tuition) + '\t\t' + str(increasedTuition) + '\t\t  ' \
          + str(money_spend) )

'''   

simple output will be like:

years: 	 Tuition Increased by: 	 Tuition:
 1		0.03		  240.0
 2		0.06		  480.0
 3		0.09		  720.0
 4		0.12		  960.0
 5		0.15		  1200.0

 
'''