#data = [22,4,234,54,2223,5,88,8]
#new = []

#while data:
    #mini = data[0]
    #for x in data:
        #if x < mini:
            #mini = x
    #new.append(mini)
    #data.remove(mini)
#print(new)

def main():
    # get the score
    scores = score()
    
    # get the total score
    total_score = total(scores)
    
    # get the lowest score
    lowest = min(scores)
    
    # subtract the lowest score
    total_score -= lowest
    
    # calculate the average score
    average = total_score / (len(scores) - 1)
    
    print('average score : ', average)
    

def total (value_list) :
    # create a variabel that holdes the total
    total = 0
    
    # create a for loop thats loop through the list and add them together
    for num in value_list:
        total += num
        
    # return the total numbers for the list
    return total

def score ():
    # create a list that holdes the user input
    test_score = []
    
    # Create a varaible that holds 
    ask_agian = 'y'
    
    # Create a while loop for counting the number of tests
    while ask_agian == 'y':
        # get the score for test
        test = int(input('Enter test score: '))
        # append the score to a list
        test_score.append(test)
        
        print('Do you want to ente another test score')
        ask_agian = input('y = yes or anything = no : ')
        
        print()
        
    return test_score 

main()