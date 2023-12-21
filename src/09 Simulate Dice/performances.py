''' Measure performances of different solutions that simulate rolling dice and
calculate the probabilities of outcomes.

Output:
Simulate rolling  of an arbitrary number of dice and calculate the results probabilities.

Time taken when using Counter class, executed 1 number of times:
          1.86177 seconds


Time taken when using pandas and numpy modules, executed 1 number of times:
          22.30827 seconds '''

import timeit
from roll_dice import roll_dice as roll_dice_monte_carlo
from roll_dice_second_solution import roll_dice as roll_dice_numpy_pandas

NUMBER_OF_RUNS = 1

# Define a setup function to call roll_dice_monte_carlo
def monte_carlo():
    dice = 4,6,6
    roll_dice_monte_carlo(dice)

# Define a setup function to call roll_dice_numpy_pandas
def numpy_pandas():
    dice = 4,6,6
    roll_dice_numpy_pandas(dice)

if __name__ == '__main__':
    print("Simulate rolling  of an arbitrary number of dice and calculate the results probabilities.")

    # Measure the time taken by Monte Carlo method
    time_monte_carlo = timeit.timeit(stmt=monte_carlo,
                                      number=NUMBER_OF_RUNS)

    print(f"\nTime taken when using Counter class, executed {NUMBER_OF_RUNS} number of times:\n\
          {round(time_monte_carlo, 5)} seconds\n")

    # Measure the time taken when using numpy and pandas functions
    time_numpy_pandass = timeit.timeit(stmt=numpy_pandas,
                                        number=NUMBER_OF_RUNS)

    print(f"\nTime taken when using pandas and numpy modules, executed {NUMBER_OF_RUNS} number of times:\n\
          {round(time_numpy_pandass, 5)} seconds\n")
