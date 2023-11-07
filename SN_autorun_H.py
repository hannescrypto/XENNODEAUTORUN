import os
import time

def clear_terminal():
    # Function to clear the terminal (platform-dependent)
    os.system('cls' if os.name == 'nt' else 'clear')

def run_syncnode():
    # Function to execute the syncnode.py script with the specific argument
    os.system('python3 syncnode.py 0x43709189a8c534ac2e65D01a2c8ceE56B702001A')

def countdown_timer(minutes, seconds):
    # Function for the countdown timer
    total_seconds = minutes * 60 + seconds
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(f'Next execution in: {timeformat}', end='\r')
        time.sleep(1)
        total_seconds -= 1

# Main function
if __name__ == "__main__":
    try:
        while True:
            clear_terminal()
            run_syncnode()
            print("syncnode.py was executed with the specific argument!")
            countdown_timer(5, 0)  # Countdown for 5 minutes
    except KeyboardInterrupt:
        print("\nScript was interrupted.")
