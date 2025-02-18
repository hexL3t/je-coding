import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Pirate's Maze Adventure")  # You can change this to your own game title
screen.bgcolor("lightblue")  # Change background color to match your theme
screen.setup(700, 700)
screen.tracer(0)  # Turn off automatic screen updates for better performance

# Create the player turtle (pirate)
player = turtle.Turtle()
player.shape("triangle")  # Change shape to represent the player (e.g., a pirate ship or character)
player.color("black")  # Change color to fit your theme
player.penup()  # Prevent the turtle from drawing lines while moving
player.speed(0)  # Set the turtle's animation speed to the fastest

# Create the goal (treasure chest)
goal = turtle.Turtle()
goal.shape("square")  # You can change this shape to anything related to your theme (e.g., treasure chest)
goal.color("gold")  # Change color to gold for treasure
goal.penup()
goal.speed(0)

# Set up the score
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()  # Hide the turtle cursor used for displaying the score
score_display.color("black")  # You can change the score color here
score_display.penup()
score_display.goto(0, 310)  # Position the score display at the top center of the screen
score_display.write(f"Treasure Found: {score}", align="center", font=("Courier", 16, "normal"))

# Create walls to form the maze
walls = []

# Function to create a wall
def create_wall(x, y, width, height):
    wall = turtle.Turtle()
    wall.speed(0)
    wall.shape("square")  # Walls are squares, but you can adjust to fit the theme (e.g., wooden planks)
    wall.color("brown")  # Change to a suitable wall color for the theme
    wall.penup()
    wall.goto(x, y)
    wall.shapesize(stretch_wid=height/20, stretch_len=width/20)  # Adjust wall size
    walls.append(wall)

# Create maze layout
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
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],  # Path with walls forming small corridors
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],  # Paths with enclosed areas and tight spaces
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],  # Narrow corridors and small open spaces
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1],  # Larger open areas and some dead ends
    [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1],  # Paths with winding corners and enclosed sections
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],  # More open spaces with complex paths
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],  # Narrow passageways and T-junctions
    [1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],  # Dead ends and longer open areas
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]   # Bottom wall
]

# Build the maze by creating walls based on the layout
for i in range(len(maze_layout)):
    for j in range(len(maze_layout[i])):
        if maze_layout[i][j] == 1:  # If the cell is a wall (value 1)
            create_wall(-250 + j*50, 250 - i*50, 50, 50)  # Create walls at specific coordinates

# Movement functions
def move_up():
    x = player.xcor()
    y = player.ycor() + 20
    if not is_collision(x, y):  # Check if there's a wall before moving
        player.goto(x, y)

def move_down():
    x = player.xcor()
    y = player.ycor() - 20
    if not is_collision(x, y):  # Check if there's a wall before moving
        player.goto(x, y)

def move_left():
    x = player.xcor() - 20
    y = player.ycor()
    if not is_collision(x, y):  # Check if there's a wall before moving
        player.goto(x, y)

def move_right():
    x = player.xcor() + 20
    y = player.ycor()
    if not is_collision(x, y):  # Check if there's a wall before moving
        player.goto(x, y)

# Check if the player is colliding with any wall
def is_collision(x, y):
    for wall in walls:
        if wall.distance(x, y) < 30:  # If the player is close to a wall
            return True
    return False

# Check if the player has reached the goal (treasure)
def check_goal():
    global score
    if player.distance(goal) < 20:  # If the player is close enough to the goal
        place_goal()  # Move the goal to a new random position
        score += 1  # Increment score
        score_display.clear()  # Clear previous score
        score_display.write(f"Treasure Found: {score}", align="center", font=("Courier", 16, "normal"))

# Place the goal (treasure chest) in a random empty spot
def place_goal():
    while True:
        x = random.randint(-5, 5) * 50  # Choose a random position for the goal
        y = random.randint(-5, 5) * 50
        if not is_collision(x, y):  # Ensure the new position is not a wall
            goal.goto(x, y)  # Set the goal's new position
            break

# Set up key bindings to move the player
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_right, "d")
screen.listen()  # Listen for key presses

# Initialize player position and place the goal
player.goto(-200, 200)
place_goal()

# Main game loop
while True:
    screen.update()  # Update the screen each loop
    check_goal()  # Check if the player has reached the goal

# Keep the window open
screen.mainloop()
