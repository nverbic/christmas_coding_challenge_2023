''' Schedule a function '''
import time
import sched
from datetime import datetime

def schedule_function(scheduled_time_in_secodns, func_name, *argv):
    ''' Schedule function call '''
    print(f"\n{func_name.__name__}() scheduled for {datetime.fromtimestamp
                            (scheduled_time_in_secodns).strftime("%A, %B %d, %Y %I:%M:%S")}\n")
    # Execute the function at the scheduled time
    s = sched.scheduler(time.time, time.sleep)
    # Schedule when you want the action to occur
    #s.enterabs(scheduled_time_in_secodns, 1, func_name(*argv))
    s.enterabs(scheduled_time_in_secodns, 1, func_name, argument=argv)
    # Block until the action has been run
    s.run()


if __name__ == '__main__':
    schedule_function(time.time()+1, print, 
                      "Scheduled function is executed after 1 sec.", "Good job!")
