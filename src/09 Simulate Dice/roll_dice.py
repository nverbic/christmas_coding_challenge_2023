''' Simulate dice 

Output:
Outcome probability for roll_dice 4, 6, 6: 

3 : 0.7%   
4 : 2.08%  
5 : 4.18%  
6 : 7.0%   
7 : 9.73%  
8 : 12.48% 
9 : 13.83% 
10 : 13.85%
11 : 12.55%
12 : 9.73% 
13 : 6.97% 
14 : 4.17% 
15 : 2.06% 
16 : 0.7%

Performance when using Counter class, code executed 1 number of times::
          0.24349 seconds'''

from random import randint
from collections import Counter
import timeit

def measure_roll_dice_performance():
    ''' Measure the performance of the function '''
    roll_dice(4,6,6)


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

    return probabilities

if __name__ == '__main__':
    probabilities = roll_dice(4,6,6)

    # Order the dictionary and print
    ordered_probabilities_by_key_asc = dict(sorted(probabilities.items()))

    # Print result
    print(f"\nOutcome probability for roll_dice 4, 6, 6: \n")
    for key, value in ordered_probabilities_by_key_asc.items():
        print(f"{key} : {value}%")

    # Measure perfromance
    time_counter_solution = timeit.timeit(setup=measure_roll_dice_performance,
                                          stmt=roll_dice,
                                          number=1)
    print(f"\nPerformance when using Counter class, code executed 1 number of times::\n\
          {round(time_counter_solution, 5)} seconds\n")
