import random

#experiment_list = []
number_of_streaks = 0
experimets_with_streaks = 0
# Code that creates a list of 100 'heads' or 'tails' values
for experiment_number in range(10000): # Run 100,00 experiments total.
   experiment_list =[]
   for i in range(100):
        toss = random.randint(0, 1)
        experiment_list.append('H' if toss == 1 else 'T') # Map 1 to 'H'

    found_streak = False #To track if this experiment has at least one streak
    i = 0
    while i <= len(experiment_list) - 6:
        if (experiment_list[i:i + 6] == ['H', 'H', 'H', 'H', 'H', 'H'] or
            experiment_list[i:i + 6] == ['T', 'T', 'T', 'T', 'T', 'T']):
            number_of_streaks += 1
            found_streak = True
            i += 6
        else:
            i += 1
    # Code that checks if ther is a streak of 6 heads or tails in a row
    if found_streak:
        experiments_with_streaks += 1 # Increment if experiment had any streaks ('break' if only calculating one streak per experiment)

# Calculate and print results
chance_of_streak = (experiments_with_streaks / 10000) * 100
print(f'Chance of streak: {chance_of_streak}%')
print(f'Total number of streaks: {number_of_streaks}')
