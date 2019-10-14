# Youssef Yatribi
# CSC119003 Intro To Programming
# February 04, 2018

# Reverse Sentence Order Program
# This program will take a sentence and output the sentence reversed

# program greeting
print('This program will display your sentence reversed')

# prompt user for sentence
senTence = input('Please type your sentence:')

# split
sen_tence = senTence.split(' ')

# display sentence
print(' '.join(reversed(sen_tence)))
