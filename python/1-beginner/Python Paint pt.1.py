import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(600, 400)  # Set the screen size (width, height)
screen.title("Simple Drawing App")  # Set the title of the window
screen.bgcolor("white")  # Set the background color of the screen

# Create the turtle
t = turtle.Turtle()
t.pensize(3)  # Set the pen size (thickness of the lines)
t.speed(0)  # Set the drawing speed to the fastest

# Color dictionary for easy access
# This dictionary maps keyboard inputs to colors
colors = {
    'r': 'red',  # 'r' key will set the turtle's pen color to red
    'g': 'green',  # 'g' key will set the turtle's pen color to green
    'b': 'blue',  # 'b' key will set the turtle's pen color to blue
    'y': 'yellow',  # 'y' key will set the turtle's pen color to yellow
    'p': 'purple',  # 'p' key will set the turtle's pen color to purple
    'o': 'orange'  # 'o' key will set the turtle's pen color to orange
}

# Set up color change functions
# This loop assigns a function to each key to change the turtle's pen color
for key, color in colors.items():
    screen.onkey(lambda c=color: t.pencolor(c), key)  # Use lambda to pass the color

# Set up drawing functions
# This makes the turtle move to the clicked position on the screen when the left mouse button is clicked
screen.onscreenclick(t.goto, 1)

# This toggles between pen up and pen down when the right mouse button is clicked
# If the pen is down, it lifts it; if the pen is up, it puts it down
screen.onscreenclick(lambda x, y: t.penup() if t.isdown() else t.pendown(), 3)

# Clear screen function
# Press the spacebar to clear the screen and reset the turtle's position
screen.onkey(lambda: (t.clear(), t.penup(), t.home()), "space")

# Enable the screen to listen for key presses
screen.listen()

# Start the drawing loop
# This keeps the turtle graphics window open and responsive
turtle.done()
