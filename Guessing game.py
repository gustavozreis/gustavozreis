print('Guessing game') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
# Three Loop Questions:
#1. What do I want to repeat?
#  -> guesses
#2. What do I want to change each time?
#  -> if it is higher or lower than the number to be guessed
#3. How long should we repeat?
#  -> 3 times


import random

num_to_guess = random.randint(1,100)

num_guessed = int(input('Guess the number (you have 10 chances): '))

if num_guessed == num_to_guess:
    print('You guessed right!')
else:

    i=0
    while i<=10:
        i+=1
        if i==10:
            print('You lost!')
            break
        elif num_guessed > num_to_guess:
            num_guessed = int(input('Your guess was to high. Try again: '))
        elif num_guessed < num_to_guess:
            num_guessed = int(input('Your guess was to Low. Try again: '))
        elif num_guessed == num_to_guess:
            print ('You guessed right!')
            break    
        
