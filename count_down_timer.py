import time
import msvcrt  # For Windows-specific input handling

# Countdown function with stop, restart, and pause functionality
def countdown(t):
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r", flush=True)

        time.sleep(1)
        t -= 1
        
        # Check for user input to pause, stop, or restart
        if input_listener():
            return
    
    print("\nFire in the hole!!")

# Function to handle user input for stop, restart, and pause (Windows-compatible)
def input_listener():
    print("\nPress 'P' to Pause, 'R' to Restart, 'S' to Stop", end="\r")

    if msvcrt.kbhit():  # Check if a key is pressed
        choice = msvcrt.getch().decode().lower()
        if choice == 'p':
            print("\nPaused. Press 'C' to Continue.")
            while True:
                if msvcrt.kbhit() and msvcrt.getch().decode().lower() == 'c':
                    print("\n Resuming...")
                    return False
        elif choice == 'r':
            print("\n Restarting the timer...")
            main()
            return True
        elif choice == 's':
            print("\nTimer Stopped!")
            return True
    return False

# Convert user input to seconds
def get_seconds():
    user_input = input("Enter time (hh:mm:ss or seconds): ").strip()
    
    if ":" in user_input:
        try:
            h, m, s = map(int, user_input.split(":"))
            return h * 3600 + m * 60 + s
        except ValueError:
            print("Invalid format! Enter time in hh:mm:ss format.")
            return get_seconds()
    else:
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input! Enter a number.")
            return get_seconds()

# Main function to run the countdown
def main():
    t = get_seconds()
    countdown(t)

# Run the program
if __name__ == "__main__":
    main()
