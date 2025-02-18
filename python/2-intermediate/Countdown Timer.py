import time
import turtle

'''def setup_turtle function sets up the Turtle graphics environment:
- It creates a screen of size 300x200 pixels and sets the title to "Countdown Timer".
- It creates a Turtle object, hides its cursor, lifts the pen (so it doesn't draw lines), and moves it to the center of the screen (0, 0).
- It returns the Turtle object for later use.'''
def setup_turtle():
    # Create a screen for the countdown timer with a specific size
    screen = turtle.Screen()
    screen.setup(300, 200)  # Set window size to 300x200 pixels
    screen.title("Countdown Timer")  # Set the window title

    # Create a turtle to display the countdown
    t = turtle.Turtle()
    t.hideturtle()  # Hide the turtle cursor so it doesn't interfere with the display
    t.penup()  # Lift the pen so the turtle doesn't draw lines while moving
    t.goto(0, 0)  # Move the turtle to the center of the screen
    return t  # Return the turtle object for further use in the countdown

'''def countdown() function performs the actual countdown:
- It takes two parameters: t (the time in seconds) and turtle_obj (the Turtle object for drawing).
- It uses a while loop that continues as long as t is greater than 0.
- In each iteration:
    - It converts the remaining seconds to minutes and seconds using divmod().
    - It formats the time as a string (e.g., "01:30" for 1 minute 30 seconds).
    - It clears the previous text and writes the new time using the Turtle object.
    - It waits for 1 second using time.sleep(1).
    - It decrements t by 1.
- After the loop ends, it displays "Time's up!".'''
def countdown(t, turtle_obj):
    # Loop until the countdown reaches 0
    while t:
        # Convert time to minutes and seconds
        mins, secs = divmod(t, 60)  # divmod() returns quotient and remainder
        timer = '{:02d}:{:02d}'.format(mins, secs)  # Format time in "mm:ss" format
        turtle_obj.clear()  # Clear the previous time display
        turtle_obj.write(timer, align="center", font=("Arial", 36, "normal"))  # Display the new time
        time.sleep(1)  # Wait for 1 second before updating the time
        t -= 1  # Decrement the time by 1 second
    
    # Once the countdown finishes, display "Time's up!"
    turtle_obj.clear()  # Clear the last time
    turtle_obj.write("Time's up!", align="center", font=("Arial", 24, "normal"))  # Display the message

''' def get_time() function prompts the user for input and validates it:
- It uses a while loop to keep asking until valid input is received.
- It uses turtle.textinput() to create a dialog box for input.
- It tries to convert the input to an integer.
- If successful and the number is positive, it returns the number.
- If the number is not positive or if there's a ValueError (non-integer input), it shows an error message and continues the loop.'''
def get_time():
    # Loop until a valid input is provided
    while True:
        try:
            # Prompt the user to enter the time in seconds using a dialog box
            seconds = int(turtle.textinput("Countdown Timer", "Enter the time in seconds:"))
            if seconds > 0:  # Check if the input is a positive number
                return seconds  # Return the valid number of seconds
            else:
                # Show an error message if the input is not positive
                turtle.textinput("Error", "Please enter a positive number.")
        except ValueError:
            # Handle non-integer input by showing an error message
            turtle.textinput("Error", "Invalid input. Please enter a number.")

''' def main() function that ties everything together:
- It calls setup_turtle() to initialize the Turtle graphics.
- It calls get_time() to get the countdown duration from the user.
- It calls countdown() with the user's input and the Turtle object.
- Finally, it calls turtle.done() to keep the window open until the user closes it.'''
def main():
    # Set up the turtle for displaying the countdown timer
    turtle_obj = setup_turtle()
    
    # Get the countdown time from the user
    seconds = get_time()
    
    # Start the countdown with the entered time
    countdown(seconds, turtle_obj)
    
    # Keep the window open after the countdown finishes
    turtle.done()

'''The last two lines ensure that the main() function is only called if the script
is run directly (not imported as a module):'''
if __name__ == '__main__':
    # Call the main function to start the countdown timer when the script is run
    main()