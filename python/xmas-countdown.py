# Import the datetime module to work with dates and times
from datetime import datetime
# Import the time module to add delays in our program
import time

# --- Time Function ---
def time_until_christmas():
    """
    Calculate the time remaining until Christmas Day (December 25th).
    
    This function finds the next occurrence of Christmas and calculates
    how many days, hours, minutes, and seconds remain until then.
    
    Returns:
        tuple: A tuple containing (days, hours, minutes, seconds) until Christmas
    """
    
    # Get the current date and time
    now = datetime.now()
    
    # Create a datetime object for Christmas of the current year
    # Format: datetime(year, month, day)
    christmas = datetime(now.year, 12, 25)
    
    # Check if Christmas has already passed this year
    # If the current time is past Christmas, we need to target next year's Christmas
    if now > christmas:
        christmas = datetime(now.year + 1, 12, 25)
    
    # Calculate the time difference (delta) between Christmas and now
    # This creates a timedelta object that stores the difference
    delta = christmas - now
    
    # Extract the number of complete days from the timedelta
    # The .days attribute gives us the total number of days
    days = delta.days
    
    # Calculate hours and remaining seconds from the leftover time
    # delta.seconds gives us the remaining seconds after removing complete days
    # divmod(a, b) returns (a // b, a % b) - the quotient and remainder
    # Dividing by 3600 (seconds in an hour) gives us hours and leftover seconds
    hours, remainder = divmod(delta.seconds, 3600)
    
    # Calculate minutes and seconds from the remaining time
    # Dividing the remainder by 60 (seconds in a minute) gives us minutes and seconds
    minutes, seconds = divmod(remainder, 60)
    
    # Return all four values as a tuple
    return days, hours, minutes, seconds

# --- Countdown Display ---
# Start an infinite loop that will run until the program is manually stopped
# (Use Ctrl+C to stop the program)
while True:
    # Call our function to get the current time until Christmas
    # Unpack the returned tuple into four separate variables
    days, hours, minutes, seconds = time_until_christmas()
    
    # Print the countdown in a formatted string
    # \r is a carriage return - moves cursor to start of line (overwrites previous line)
    # f-string allows us to embed variables directly in the string
    # :02 formats numbers with leading zeros (e.g., 5 becomes 05)
    # end='' prevents moving to a new line, keeping the countdown on one line
    print(f"\r{days} days {hours:02} hours {minutes:02} mins {seconds:02} secs", end='')
    
    # Pause the program for 1 second before the next update
    # This creates the "ticking" effect of a real countdown timer
    time.sleep(1)