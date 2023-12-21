''' Simulate dice 

Output:
Outcome probability for roll_dice (4, 6, 6), 1000000 rolls 
Total
3 : 0.69%
4 : 2.07%
5 : 4.17%
6 : 6.92%
7 : 9.73%
8 : 12.5%
9 : 13.83%
10 : 13.91%
11 : 12.56%
12 : 9.73%
13 : 6.95%
14 : 4.17%
15 : 2.07%
16 : 0.69%
'''

from random import randint
from collections import Counter

NUM_SIMULATIONS = 1000000

def roll_dice(dice):
    '''  Takes a variable number of input arguments representing 
    the number of sides on an arbitrary number of dice. '''
    results = []

    for _ in range(NUM_SIMULATIONS):
        sum_dice_results = 0
        for die in dice:
            sum_dice_results += randint(1, die)
        results.append(sum_dice_results)

    # Count the number of times a specific result occurs,
    # and store the results as keys and the counts as values.
    result_counts = Counter(results)

    # Calculate the probability by dividing result count by total number of simulations.
    probabilities = {key: round((count / NUM_SIMULATIONS)*100, 2) for
                     key, count in result_counts.items()}

    # Order the dictionary
    ordered_probabilities = dict(sorted(probabilities.items()))

    return ordered_probabilities

if __name__ == '__main__':
    # Choose an arbitrary set of dice
    dice = 4,6,6
    probabilities = roll_dice(dice)

    # Print result
    print(f"\nOutcome probability for roll_dice {dice}, {NUM_SIMULATIONS} rolls \nTotal")
    for key, value in probabilities.items():
        print(f"{key} : {value}%")

