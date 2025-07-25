# The following program is meant to be a simple coin toss guessing game. The player gets two guesses.
#(It’s an easy game.) However, the program has multiple bugs in it.
#Run through the program a few times to find the bugs that keep the program from working correctly.
import random

#Mapping strings to intergers
heads = 1
tails = 0

#Ask for first guess
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower()

# Simulate the coin toss
toss = random.randint(0, 1)  # 0 is tails, 1 is heads

# Convert guess to number
if guess == 'heads':
    guess_num = 1
else:
    guess_num = 0

#First guess check
if toss == guess_num:
    print('You got it!')
else:
    print('Nope! Guess again!')

    # Second guess
    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input().lower()

    if guess == 'heads':
        guess_num = 1
    else:
        guess_num = 0

    if toss == guess_num:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
