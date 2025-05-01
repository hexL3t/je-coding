# Countdown Timer
# Import Libaries
import time

# ASCII ART TITLE
# /,|][*%&^
print("""
********************************
*                              *
*      COUNTDOWN TIMER         *
*                              *
********************************
""")

# Ask the user for the number of seconds to countdown
seconds = int(input("How many seconds until launch?: "))

# Start the countdown loop
while seconds > 0:
    # Calculate minutes and seconds for display
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    
    # Python Operators
    # + : Addition
    # - : Subtraction
    # * : Multiplication
    # / : Division
    # % : Modulus (Finds the remainder after the division of two numbers)
    # ** : Exponentiation/Power (Returns first raised to power second)
    # // : Floor Division (Divides the first number by the second - rounding)
    
    # Create a formatted time string
    # Formatted String / F-String : Allows you to format strings in a simple
    # and clear way. Allows you to embed variables and expressions inside a
    # string.
    time_display = f"{minutes:02d}:{remaining_seconds:02d}"
    # The :02d part makes sure that we are always showing two digits.
    
    #Print the current time remaining
    print(f"Time Remaining: {time_display}")
    
    # wait 1 second
    time.sleep(1)
    
    # Decrease the remaining time by 1 second
    seconds -= 1   # < seconds = seconds - 1
    
    #Add some excitement as we get closer to launch
    #if seconds == 10:
       # print("10 seconds to launch")
    #elif seconds == 5:
       # print("Ignition sequence started!")
        
# Countdown Timer Finished
#print("Blast Off! 🚀")