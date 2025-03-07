# Countdown Timer with Pause, Restart, and Stop Functionality

## Description
This Python script is a countdown timer that allows the user to enter a time duration and provides the ability to **pause, restart, or stop** the countdown. The program is **Windows-compatible**, using `msvcrt` for real-time keyboard input handling.

## Features
- **Input Time in Various Formats**: Accepts input in both `hh:mm:ss` format and as total seconds.
- **Real-Time User Controls**:
  - `P` - Pause the countdown.
  - `C` - Continue after pausing.
  - `R` - Restart the countdown.
  - `S` - Stop the countdown.
- **Dynamic Display**: Updates the countdown in real time.

## Installation
Ensure you have Python installed on your system. No additional libraries are required since this script only uses built-in modules.

## Usage
1. **Run the script**
   ```sh
   python countdown.py
   ```
2. **Enter the countdown time** in one of the following formats:
   - `hh:mm:ss` (e.g., `00:02:30` for 2 minutes 30 seconds)
   - Total seconds (e.g., `150` for 150 seconds)
3. **During countdown**, you can press:
   - `P` to pause
   - `C` to continue after pausing
   - `R` to restart the countdown
   - `S` to stop the countdown

## Example Run
```
Enter time (hh:mm:ss or seconds): 00:01:30
01:30
Press 'P' to Pause, 'R' to Restart, 'S' to Stop

(P is pressed)

⏸️ Paused. Press 'C' to Continue.
(C is pressed)
▶️ Resuming...

(Countdown completes)
🔥 Fire in the hole!! 🔥
```

## Notes
- This script **only works on Windows** due to its use of `msvcrt` for keyboard input.
- The script runs continuously until the countdown completes or the user stops it.
- If an invalid time format is entered, the script prompts the user to re-enter a valid format.

## License
This project is free to use and modify.

---
Feel free to enhance it by adding additional features like sound alerts or cross-platform compatibility!

