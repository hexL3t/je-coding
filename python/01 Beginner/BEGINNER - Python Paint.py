import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(600, 400)
screen.title("Simple Drawing App")
screen.bgcolor("white")

# Create the turtle
t = turtle.Turtle()
t.pensize(3)
t.speed(0)  # Fastest drawing speed

# Color dictionary
colors = {
    'r': 'red',
    'g': 'green',
    'b': 'blue',
    'y': 'yellow',
    'p': 'purple',
    'o': 'orange'
}

# Set up color change functions
for key, color in colors.items():
    screen.onkey(lambda c=color: t.pencolor(c), key)

# Set up drawing functions
screen.onscreenclick(t.goto, 1)
screen.onscreenclick(lambda x, y: t.penup() if t.isdown() else t.pendown(), 3)

# Clear screen function
screen.onkey(lambda: (t.clear(), t.penup(), t.home()), "space")

# Enable keys
screen.listen()

# Start the drawing loop
turtle.done()