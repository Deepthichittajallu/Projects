import random
print('Welcome to Number guessing game!! You will get 7 chnces to guess the number.')
print('Choose wisely')
num=random.randrange(100)
chances=7
guess_count=0;
while(guess_count<chances):
    guess_count+=1
    guess=int(input("Enter the number you wish in the range"))
    if(num==guess):
        print('Congratulations! you have guessed correctly the number {} in {} attempt'.format(num,guess_count))
        break
    elif(guess_count>chances and num!=guess):
        print('Oops! you have lost the game.Betterluck next time')
    elif(guess>num):
        print('You have guessed too high')
    elif(guess<num):
        print('You have guessed too low')
