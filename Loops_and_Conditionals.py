# 4.1
# Choosing random number between 1 and 10


def string_or_integer(guess):
    while True:
        if guess in ('quit', 'Quit'):
            print('Bye!')
            sys.exit()
        elif not guess in ('quit', 'Quit'):
            try:
                return int(guess)
            except ValueError:
                try:
                    float(guess)
                    print("Please use whole numbers")
                    guess = input('>>> ')
                except ValueError:
                    print ("Please enter a number between 1 and 10")
                    guess = input('>>> ')
 
def game():
    guess = input('>>> ')
    secret = string_or_integer(guess)
    if (secret == rNum):
        print('just right')
        sys.exit()
    elif (secret > 10):
        print('low')
        game()
    elif (secret < rNum):
        print('Try a higher number')
        game()
    elif (secret > rNum):
        print('too high')
        game()
 
import random
import sys
rNum = random.randint(1,10)
print('Welcome\nGuess a number between 1 and 10\nTo give up, type "quit"')
game()