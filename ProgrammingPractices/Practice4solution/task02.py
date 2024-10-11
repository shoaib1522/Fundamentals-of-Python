import random
x = random.randint(1,10) 
guess_1=int(input('Guess the number chance 1'))
guess_2=int(input('Guess the number chance 2'))
guess_3=int(input('Guess the number chance 3'))
if(guess_1==x):
    print('winner')
elif(guess_2==x):
    print('winner')
elif(guess_3==x):
    print('winner')
else:
    print('loser')
    print('number is',x)