# Import the datetime module to work with dates and times
from datetime import datetime
# Import turtle graphics library for creating visual elements
import turtle
# Import random module (imported but not used in this version)
import random

# --- Screen Setup ---
# Create the main turtle graphics window
screen = turtle.Screen()

# Set the window title that appears in the title bar
screen.title("Christmas Countdown")

# Set background color to sky blue using hex color code
# #87CEEB is a light blue representing a clear summer sky
screen.bgcolor("#87CEEB")

# Set the dimensions of the window in pixels (width x height)
screen.setup(width=750, height=350)

# Turn off automatic screen updates for better performance
# We'll manually update the screen when we want changes to appear
# This prevents flickering and makes animations smoother
screen.tracer(False)

# --- Sand Base at Bottom ---
# Create a turtle object to draw the sand at the bottom of the screen
sand = turtle.Turtle()

# Hide the turtle cursor (arrow) since we only want to see the drawing
sand.hideturtle()

# Lift the pen up so we can move without drawing
sand.penup()

# Move to the bottom-left corner of the screen
# Coordinates: x=-375 (half of 750 width), y=-175 (bottom of screen)
sand.goto(-375, -175)

# Point the turtle to the right (0 degrees is east/right)
sand.setheading(0)

# Set the color to "wheat" - a sandy beige color
sand.color("wheat")

# Begin filling the shape we're about to draw
sand.begin_fill()

# Put the pen down to start drawing
sand.pendown()

# Draw a rectangle for the sand by moving in a square pattern:
sand.forward(750)   # Draw right edge (full width of screen)
sand.left(90)       # Turn left (now facing up)
sand.forward(80)    # Draw upward (height of sand)
sand.left(90)       # Turn left (now facing left)
sand.forward(750)   # Draw left edge
sand.left(90)       # Turn left (now facing down)
sand.forward(80)    # Draw downward
sand.left(90)       # Turn left (back to original orientation)

# Fill the rectangle with the wheat color
sand.end_fill()

# --- Countdown Display ---
# Create a turtle object for writing text (the countdown timer)
pen = turtle.Turtle()

# Hide the turtle cursor since we only want to see text
pen.hideturtle()

# Lift the pen - we'll only use this turtle for writing, not drawing lines
pen.penup()

# --- Time Functions ---
def time_until_christmas():
    """
    Calculate the time remaining until Christmas Day (December 25th).
    
    This function is similar to Part 1, but now also returns the
    current time and Christmas date objects for display purposes.
    
    Returns:
        tuple: (now, christmas, days, hours, minutes, seconds)
               - now: current datetime object
               - christmas: next Christmas datetime object
               - days: complete days remaining
               - hours: hours remaining (0-23)
               - minutes: minutes remaining (0-59)
               - seconds: seconds remaining (0-59)
    """
    
    # Get the current date and time
    now = datetime.now()
    
    # Create a datetime object for Christmas of the current year
    christmas = datetime(now.year, 12, 25)
    
    # If Christmas has already passed this year, target next year
    if now > christmas:
        christmas = datetime(now.year + 1, 12, 25)
    
    # Calculate the time difference between Christmas and now
    delta = christmas - now
    
    # Extract days from the timedelta object
    days = delta.days
    
    # Calculate hours and remaining seconds
    # divmod returns (quotient, remainder) when dividing
    hours, remainder = divmod(delta.seconds, 3600)
    
    # Calculate minutes and seconds from the remainder
    minutes, seconds = divmod(remainder, 60)
    
    # Return all values including the datetime objects
    return now, christmas, days, hours, minutes, seconds

# --- Countdown Text Update ---
def update_countdown():
    """
    Update the countdown display on the screen.
    
    This function:
    1. Clears the previous text
    2. Gets the current time until Christmas
    3. Displays formatted countdown text at different positions
    4. Shows a special message if it's Christmas Day
    5. Schedules itself to run again in 1 second
    """
    
    # Clear any previous text written by this turtle
    # This prevents text from overlapping on each update
    pen.clear()
    
    # Get the current countdown values
    now, christmas, days, hours, minutes, seconds = time_until_christmas()
    
    # --- Display Header Text ---
    # Move the pen to position (0, 60) - center horizontally, upper area
    pen.goto(0, 60)
    
    # Set text color to dark blue using hex color code
    pen.color("#004e89")
    
    # Write the header text
    # align="center" centers the text on the x-coordinate
    # font tuple: (family, size, style)
    pen.write("There are only...", align="center", font=("Arial", 16, "bold"))
    
    # --- Display Main Countdown ---
    # Change color to white for the countdown numbers
    pen.color("#ffffff")
    
    # Move to center of screen for the main countdown
    pen.goto(0, 0)
    
    # Write the countdown using an f-string for formatting
    # :02 ensures two digits with leading zeros (e.g., 05 instead of 5)
    pen.write(f"{days} days {hours:02} hours {minutes:02} mins {seconds:02} secs",
              align="center", font=("Courier", 26, "bold"))
    
    # --- Display Footer Text ---
    # Move below the countdown for the target message
    pen.goto(0, -40)
    
    # Set color back to dark blue
    pen.color("#004e89")
    
    # Write the target date message
    pen.write(f"Until Christmas!",
              align="center", font=("Arial", 16, "bold"))
    
    # --- Special Christmas Day Message ---
    # Check if we've reached Christmas (all values are zero)
    if days == 0 and hours == 0 and minutes == 0 and seconds == 0:
        # Move to lower position for special message
        pen.goto(0, -140)
        
        # Set color to dark green (#006400)
        pen.color("#006400")
        
        # Display the Christmas greeting
        pen.write("MERRY CHRISTMAS!", align="center", font=("Arial", 22, "bold"))
    
    # Manually update the screen to show all our changes at once
    # This is necessary because we set tracer(False) earlier
    screen.update()
    
    # Schedule this function to run again after 1000 milliseconds (1 second)
    # This creates a loop that updates the countdown every second
    # ontimer is better than a while loop because it doesn't block the GUI
    screen.ontimer(update_countdown, 1000)

# --- Sun Decoration ---
# Create a turtle to draw a decorative sun
sun = turtle.Turtle()

# Hide the turtle cursor
sun.hideturtle()

# Lift the pen for positioning
sun.penup()

# Position the sun in the upper right area of the sky
# Coordinates: x=250 (right side), y=80 (upper area)
sun.goto(250, 80)

# Set the sun color to yellow
sun.color("yellow")

# Begin filling the circle shape
sun.begin_fill()

# Draw a circle with radius 40 pixels
# The circle is drawn counterclockwise from the current position
sun.circle(40)

# Fill the circle with yellow color
sun.end_fill()

# --- Start Everything ---
# Call the update_countdown function to start the countdown display
# This initiates the recursive timer loop
update_countdown()

# Start the turtle graphics event loop
# This keeps the window open and responsive to events
# The program will run until the user closes the window
screen.mainloop()