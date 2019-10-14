# Youssef Yatribi
# CSC119.101
# Feb 22, 2018
#
# Magic Eight Ball simulator
#

def getQuestion():
    question = input('What is your question?:\n')
    print('\nYou ask me ', '"' + question + '". . .')
    time.sleep(1)
    print('hmmmm ... let me think about that')
    time.sleep(2)
    
    if 'Why' in question or 'Why?' in question or 'why' in question:
        print('Why not?')
    if 'I' in question or 'How' in question or 'how' in question:
        print('The odds are in your favor')
    if 'So' in question or 'diffrence' or 'to' in question:
        print('Let me think about it')
    if 'Do' in question or 'do' in question:
        print('Makes sense to me')
    else:
        randomResponse = random.randint(1,8)
        if randomResponse == 1:
            print('... the probabilities are in your favor ...')
        if randomResponse == 2:
            print('... make no definite plans ...')
        if randomResponse == 3:
            print('... the answer is hazy ...')
        if randomResponse == 4:
            print('... you already know the answer...')
        if randomResponse == 5:
            print('... the answer is in your morning cereal...')
        if randomResponse == 6:
            print('... your chances are slim...')
        if randomResponse == 7:
            print('...chances are yes...')
        if randomResponse == 8:
            print('... chances are no...')
        return question
def giveResponse():                  
    more = input('\nWould you like to ask another question? (y/n) ')
    if more != 'y' and more != 'Y':
        keepGoing = False
    if more == 'y':
        return True
    else:
        return False

import random
import time
getQuestion()
keepGoing = True
while keepGoing:
     giveResponse()
     print()
     keepGoing = giveResponse()
print('\n\nThank you for using the NOT Magic Eight Ball.')
print('May all your answers be true.')
print('May the schwartz be with you')    
        
    
