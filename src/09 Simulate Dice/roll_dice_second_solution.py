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

Outcome probability for roll_dice (4, 6, 6), 1000000 rolls
Total
3     0.01
4     0.02
5     0.04
6     0.07
7     0.10
8     0.12
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
import matplotlib.pyplot as plt
import seaborn as sb

NUM_SIMULATIONS = 1000000

def plot_histogram_seaborn(totals):
    '''Plot distribution of a dataset (totals)'''

    sb.set_style('whitegrid')
    sb.histplot(totals, kde=True, color='salmon', edgecolor='black')
    plt.show()

def plot_line_chart_seaborn(probabilities, num_dice, num_rolls):
    ''' Plotting the probabilities'''

    sb.set_style('whitegrid')

    # Plotting the probabilities using seaborn
    #sb.barplot(x=probabilities.index, y=probabilities.values, color='blue', alpha=0.7)

    # Plotting the probabilities using seaborn - simpler solution
    sb.lineplot(data=probabilities, marker='o', color='blue')

    # Add grid
    plt.grid(color='gray', linestyle='--', linewidth=0.5)

    # Plot all of the x values as x ticks
    plt.xticks(probabilities.index)

    plt.title(f'Rolling dice simulation: {num_dice} dice, {num_rolls} rolls')
    plt.xlabel('Result')
    plt.ylabel('Probability')
    plt.show()

def plot_bar_chart_pyplot(probabilities, num_dice, num_rolls):
    ''' Plotting the probabilities'''

    # Plotting the probabilities using matplotlib pyplot
    probabilities.plot(kind='bar')

    plt.xlabel('Result')
    plt.ylabel('Probability')
    plt.title(f'Rolling dice simulation: {num_dice} dice, {num_rolls} rolls')
    plt.show()

def plot_pie_chart_pyplot(probabilities, num_dice, num_rolls):
    ''' Plotting the probabilities'''

    plt.figure(figsize=(8, 8))

    # Plotting the probabilities using matplotlib pyplot
    plt.pie(probabilities, labels=probabilities.index)

    plt.title(f'Rolling dice simulation: {num_dice} dice, {num_rolls} rolls')

    # Create a custom legend with probabilities
    legend_labels = [f'{index} ({value})' for index, value in zip(probabilities.index, probabilities)]
    plt.legend(legend_labels, title='Total Probabilities', loc='best', bbox_to_anchor=(1, 0.5))
    plt.show()


def simulate_dice_rolls(dice, num_simulations):
    '''  Simualte dice rolls
         dice = number of sides on an arbitrary number of dice. '''

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

def roll_dice(dice):
    '''  Simulate dice rolls and calculate probabilities of possible outcomes '''

    # Roll dice and return results in a DataFrame object
    dice_results_df = simulate_dice_rolls(np.array(dice), NUM_SIMULATIONS)

    # Temporarily commented - measuring the performance
    # print("Simulation results,\n the first 10 rows:")
    # print(dice_results_df.head(10))
    # print("\nand the last 10 rows:")
    # print(dice_results_df.tail(10))

    # Calculate probabilities based on the simulation results
    # The value_counts method is used to calculate the frequencies 
    # of unique values in a specific column.
    probabilities = dice_results_df['Total'].value_counts(normalize=True).sort_index().round(2)

    return probabilities

if __name__ == '__main__':
    # Calculate probabilities
    dice = 4,6,6
    probabilities = roll_dice(dice)

    # Print the result
    print(f"\nOutcome probability for roll_dice {dice}, {NUM_SIMULATIONS} rolls")
    print(probabilities)

    # Plot
    plot_bar_chart_pyplot(probabilities,3, NUM_SIMULATIONS)
    plot_line_chart_seaborn(probabilities, 3, NUM_SIMULATIONS)
    plot_pie_chart_pyplot(probabilities, 3, NUM_SIMULATIONS)

    # Temporarily commented - measuring the performance
    # plot_histogram_seaborn(dice_results_df['Total'])
