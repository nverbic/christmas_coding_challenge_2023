''' Simulate dice 

Output:
Outcome probability for roll_dice(4, 6, 6):

3 : 0.69%
4 : 2.09%
5 : 4.15%
6 : 6.93%
7 : 9.76%
8 : 12.49%
9 : 13.85%
10 : 13.91%
11 : 12.52%
12 : 9.73%
13 : 7.0%
14 : 4.14%
15 : 2.08%
16 : 0.68%'''

from random import randint
from collections import Counter

def roll_dice(*args):
    '''  Takes a variable number of input arguments representing 
    the number of sides on an arbitrary number of dice. '''
    results = []
    num_simulations = 1000000

    for _ in range(num_simulations):
        sum_dice_results = 0
        for dice in args:
            sum_dice_results += randint(1, dice)
        results.append(sum_dice_results)

    # Count the number of times a specific result occurs,
    # and store the results as keys and the counts as values.
    result_counts = Counter(results)

    # Calculate the probability by dividing result count by total number of simulations.
    probabilities = {key: round((count / num_simulations)*100, 2) for
                     key, count in result_counts.items()}

    # Order the dictionary and print
    ordered_probabilities_by_key_asc = dict(sorted(probabilities.items()))
    print(f"\nOutcome probability for roll_dice{args}: \n")
    for key, value in ordered_probabilities_by_key_asc.items():
        print(f"{key} : {value}%")

if __name__ == '__main__':
    roll_dice(4,6,6)
