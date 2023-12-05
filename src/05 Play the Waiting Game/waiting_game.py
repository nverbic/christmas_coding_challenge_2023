'''Waiting game. 

Output:
Welcome to waiting game --->


Your target time is 3 seconds
 ---Press Enter to Begin---


...Press Enter again after 3 seconds...


Elapsed time: 3.009 seconds
(0.009 seconds too slow)'''

import time
import random

def waiting_game():
    ''' Waiting game '''
    print("\nWelcome to waiting game --->\n\n")
    # Generate random number of seconds
    seconds = random.randint(2, 4)
    print(f"Your target time is {seconds} seconds")
    input(" ---Press Enter to Begin---\n\n")
    start_time = time.time()
    input(f"...Press Enter again after {seconds} seconds...\n\n")
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = round(end_time - start_time, 3)
    print(f"Elapsed time: {elapsed_time} seconds")

    # Calculate the difference between the elapsed time and the target time
    difference = round(seconds - elapsed_time, 3)
    if difference > 0:
        print(f"({abs(difference)} seconds too fast)\n")
    elif difference < 0:
        print(f"({abs(difference)} seconds too slow)\n")
    else:
        print("Bravo! Perfect timing!!!\n")


if __name__ == '__main__':
    waiting_game()
