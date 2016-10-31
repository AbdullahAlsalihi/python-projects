# Abdullah Al-Salihi
# CSC - 212
'''
An acronym is a word formed by taking the first letters	of the
words in a phrase and making a word from them. For example,
RAM is an acronym for “random access memory.” Write a
program that allows the user to type in a phrase and then
outputs the acronym for that phrase. Note: the acronym
should be all uppercase, even if the words in the phrase are not
capitalized.
'''
# Creating a userInput String that hold the user input
# Using the split method to allow the user to enter a space
# For separating the words (of the user will input).

userInput = input('Please Enter a word: ').split(' ')

# Creating empty string that will hold each character in the loop
words = ''

# Creating a for loop to loop through the words that the user input
# Storing the first letter for each word and combined it to gather
# Output the result in upper case weather the user input it or not

for i in userInput:
    words = i[0]
    print(words.upper(), end='')

