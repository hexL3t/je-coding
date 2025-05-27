import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Watermelon Labyrith Game")
screen.bgcolor("paleturquoise")
screen.setup(700, 700)
screen.tracer(0)  # Turn off automatic screen updates

# Create the player turtle (ghost)
player = turtle.Turtle()
player.shape("circle")
player.color("white")
player.penup()  # Prevent the turtle from drawing lines
player.speed(0)  # Set the turtle's animation speed to the fastest

# Create the goal (pumpkin)
goal = turtle.Turtle()
goal.shape("circle")
goal.color("green")
goal.penup()
goal.speed(0)

# Set up the score
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()  # Hide the turtle cursor
score_display.color("green")
score_display.penup()
score_display.goto(0, 310)  # Position the score display
score_display.write(f"Watermelons Collected: {score}", align="center", font=("Courier", 16, "normal"))

# Create walls
walls = []

def create_wall(x, y, width, height):
    wall = turtle.Turtle()
    wall.speed(0)
    wall.shape("square")
    wall.color("cornsilk")
    wall.penup()
    wall.goto(x, y)
    wall.shapesize(stretch_wid=height/20, stretch_len=width/20)  # Adjust wall size
    walls.append(wall)


# Create maze layout (a 2D array representing the maze)
""" Create maze layout (2D array representing the maze)
Each row in 2D array represents a horizontal line in the maze
Each element in a row represents a specific position:
      1 : Represents a Wall blocking the player's movement
      0 : Represents a path, allowing the player to move through

By using Binary Values, you can visualise the structure of the maze.
     Walls : The outer edges of the array, as well as speciific internal
             positions, to form the walls of the maze
     Paths: The 0s create paths that you can navigate through.

This is the easist method to generate a maze layout using code."""

maze_layout = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Top wall
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],  # Path with a wall in the middle
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],  # Path with walls and a small enclosed area
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],  # Path with a long corridor
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],  # Path with a T-junction
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],  # Path with a wall in the middle
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1],  # Path with a small enclosed area
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1],  # Path with a large enclosed area
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],  # Path with a small enclosed area
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],  # Path with a long corridor
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]   # Bottom wall
]

# Build the maze
for i in range(len(maze_layout)):
    for j in range(len(maze_layout[i])):
        if maze_layout[i][j] == 1:  # If the cell is a wall
            create_wall(-250 + j*50, 250 - i*50, 50, 50)

# Movement functions
def move_up():
    x = player.xcor()
    y = player.ycor() + 20
    if not is_collision(x, y):  # Check for collision before moving
        player.goto(x, y)
        
def move_down():
    x = player.xcor()
    y = player.ycor() - 20
    if not is_collision(x, y):  # Check for collision before moving
        player.goto(x, y)

def move_left():
    x = player.xcor() - 20
    y = player.ycor()
    if not is_collision(x, y):  # Check for collision before moving
        player.goto(x, y)

def move_right():
    x = player.xcor() + 20
    y = player.ycor()
    if not is_collision(x, y):  # Check for collision before moving
        player.goto(x, y)

# Check for collision with walls
def is_collision(x, y):
    for wall in walls:
        if wall.distance(x, y) < 30:  # Check if the player is close enough to a wall
            return True
    return False

# Check for collision with goal
def check_goal():
    global score
    if player.distance(goal) < 20:  # Check if the player is close enough to the goal
        place_goal()  # Move the goal to a new random position
        score += 1
        score_display.clear()
        score_display.write(f"Watermelons Collected: {score}", align="center", font=("Courier", 16, "normal"))

# Place goal in a random empty spot
def place_goal():
    while True:
        x = random.randint(-5, 5) * 50
        y = random.randint(-5, 5) * 50
        if not is_collision(x, y):  # Check if the new position is valid
            goal.goto(x, y)
            break

# Set up key bindings
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_right, "d")
screen.listen()

# Initialize player and goal positions
player.goto(-200, 200)
place_goal()

# Main game loop
while True:
    screen.update()  # Update the screen
    check_goal()

# Keep the window open (this line is not reached in this example)
screen.mainloop()