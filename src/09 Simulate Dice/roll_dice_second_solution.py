''' Simulate dice 

Output:
Simulation results (first 10 rows):
       Rolls  Total
0  (4, 4, 3)     11
1  (1, 3, 5)      9
2  (3, 3, 6)     12
3  (2, 6, 3)     11
4  (1, 1, 3)      5
5  (4, 3, 6)     13
6  (2, 5, 1)      8
7  (4, 1, 3)      8
8  (3, 3, 3)      9
9  (2, 4, 6)     12

Probabilities:
Total
3     0.01
4     0.02
5     0.04
6     0.07
7     0.10
8     0.13
9     0.14
10    0.14
11    0.13
12    0.10
13    0.07
14    0.04
15    0.02
16    0.01
'''

import numpy as np
import pandas as pd

def simulate_dice_rolls(dice):
    '''  Simualte dice rolls
         dice = number of sides on an arbitrary number of dice. '''

    num_simulations = 1000000
    rolls = []

    # Roll dice
    for _ in range(num_simulations):
        roll = np.random.randint(1, dice + 1, size=len(dice))
        rolls.append(roll)

    # Calculate the sum of each row
    results = np.sum(rolls, axis=1)

     # Create a DataFrame to organize the results
    results_df = pd.DataFrame({'Rolls': [tuple(row) for row in rolls],
                              'Total': results})

    return results_df


def roll_dice(*args):
    '''  Simulate dice rolls and calculate probabilities of possible outcomes '''

    # Roll dice and return results in a DataFrame object
    dice_results_df = simulate_dice_rolls(np.array(args))

    print("Simulation results (first 10 rows):")
    print(dice_results_df.head(10))

    # Calculate probabilities based on the simulation results
    # The value_counts method is used to calculate the frequencies 
    # of unique values in a specific column.
    probabilities = dice_results_df['Total'].value_counts(normalize=True).sort_index().round(2)

    print("\nProbabilities:")
    print(probabilities)

if __name__ == '__main__':
    roll_dice(4,6,6)
