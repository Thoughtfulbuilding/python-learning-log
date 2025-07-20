# chapter 4 practice question. Why does each function call return the same number?
import random
random_number = random.randint(1, 6)

def get_random_dice_roll():
    # Returns a random interger from 1-6
    #random_number = random.randint(1, 6) <--- variable should be placed here to repeat. It is only determined once in global scope.
    return random_number

print(get_random_dice_roll())
print(get_random_dice_roll())# Write your code here :-)
print(get_random_dice_roll())
print(get_random_dice_roll())
