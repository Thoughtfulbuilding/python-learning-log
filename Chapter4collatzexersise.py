# Write your code here :-)
import random, sys

def collatz(number):
    while number !=1:
        if number % 2==0:
            number = number//2
            print(number, end=' ')
        else:
            number = 3 * number + 1
            print(number, end=' ')
    print('\nreached 1. Exiting...')


#number = random.randint(0, 1000)
#int('random number',':', number)
print('Please enter random interger.')

try:
    number = int(input('>'))
    if number < 1:
        print('Please enter a number greater than 0.')
    else:
        collatz(number)
except ValueError:
        print('Please enter interger')



