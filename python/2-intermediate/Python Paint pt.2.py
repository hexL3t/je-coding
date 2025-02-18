import turtle

# Setup the drawing screen
def setup_screen():
    screen = turtle.Screen()  # Create a screen object
    screen.setup(600, 400)  # Set screen size
    screen.title("Advanced Drawing App")  # Set window title
    screen.bgcolor("white")  # Set background color of the screen
    return screen

# Create and configure a turtle object for drawing
def create_turtle():
    t = turtle.Turtle()  # Create a turtle object
    t.pensize(3)  # Set the size of the drawing pen
    t.speed(0)  # Set the turtle's speed to fastest (0 = no animation)
    return t

# Change the turtle's pen color
def change_color(color):
    t.pencolor(color)  # Change the pen color to the passed color

# Toggle the pen state (up/down)
def toggle_pen():
    if t.isdown():  # If the pen is down (drawing)
        t.penup()  # Lift the pen
    else:
        t.pendown()  # Lower the pen to start drawing

# Start drawing at the given coordinates (click event handler)
def start_drawing(x, y):
    t.pendown()  # Put the pen down to start drawing
    t.goto(x, y)  # Move the turtle to the click position

# Draw a line to the clicked coordinates
def draw(x, y):
    t.goto(x, y)  # Move the turtle to the new coordinates and draw

# Erase a drawing at the clicked location
def erase(x, y):
    pen_color = t.pencolor()  # Store the current pen color
    pen_size = t.pensize()  # Store the current pen size
    t.pencolor("white")  # Set the pen color to white (for erasing)
    t.pensize(10)  # Set a larger pen size for erasing
    t.goto(x, y)  # Move to the clicked location
    t.pencolor(pen_color)  # Restore the original pen color
    t.pensize(pen_size)  # Restore the original pen size

# Draw a left curve (using turtle's circle method)
def curve_left():
    t.circle(50, 45)  # Draw a curve with radius 50 and angle 45 degrees

# Draw a right curve (using turtle's circle method with negative radius)
def curve_right():
    t.circle(-50, 45)  # Draw a curve in the opposite direction

# Clear the entire screen
def clear_screen():
    t.clear()  # Clear all drawings on the screen
    t.penup()  # Lift the pen so it doesn’t draw anything while resetting
    t.home()  # Move the turtle to the center of the screen

# Main function to run the app
def main():
    global screen, t  # Declare global variables to access screen and turtle
    screen = setup_screen()  # Set up the screen
    t = create_turtle()  # Create the turtle for drawing

    # Mapping of keys to colors
    color_keys = {
        'r': 'red', 'g': 'green', 'b': 'blue',
        'y': 'yellow', 'p': 'purple', 'o': 'orange', 'w': 'white'
    }

    # Create a turtle to display the color commands on the screen
    color_commands = turtle.Turtle()
    color_commands.penup()  # Lift the pen so it doesn't draw anything
    color_commands.goto(-280, -160)  # Position it to the left of the screen
    color_commands.write("Color Commands:", font=("Arial", 10, "bold"))  # Display a title
    color_commands.penup()
    color_commands.goto(-280, -180)  # Move it down for the color options

    # Display each color command on the screen in a straight line
    for key, color in color_keys.items():
        screen.onkey(lambda c=color: change_color(c), key)  # Assign a key press to each color
        color_commands.write(f"{key.upper()} : {color}", font=("Arial", 8))  # Display color option
        color_commands.setx(color_commands.xcor() + 80)  # Move the text to the right for next color

    color_commands.hideturtle()  # Hide the helper turtle after displaying the options

    # Setup screen events
    screen.onscreenclick(start_drawing, 1)  # Left click starts drawing
    screen.onscreenclick(lambda x, y: toggle_pen(), 3)  # Right click toggles the pen up/down
    screen.onkey(clear_screen, "space")  # Space bar clears the screen
    screen.onkey(curve_left, "Left")  # Left arrow key draws a left curve
    screen.onkey(curve_right, "Right")  # Right arrow key draws a right curve
    screen.listen()  # Start listening for key events

    # Enable dragging the turtle to draw
    t.ondrag(draw)

    # Setup eraser mode (currently hidden turtle, could be implemented later)
    eraser_turtle = turtle.Turtle()
    eraser_turtle.hideturtle()  # Hide the turtle for the eraser mode
    eraser_turtle.penup()

    turtle.done()  # Finish the turtle graphics and keep the window open

# Start the program when this script is run
if __name__ == "__main__":
    main()