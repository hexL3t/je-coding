# Turtle  Dodge
# Import Libraries
import turtle
import random
import time

# Setup Game Screen
screen = turtle.Screen()
# screen.title("Turtle Dodge")
screen.bgcolor("lightgreen")
screen.setup(600, 600)
screen.tracer(0) # Turn off automatic screen updates

# Player Set Up
player = turtle.Turtle()
player.shape("turtle")
player.color("dark red") # Pick Your Favourite Title
player.penup()
player.goto(-250, 250) # Sets the player to the top left of game screen

# Goal Setup (gold coin, dorito?, sandwich/lettuce)
goal = turtle.Turtle()
goal.shape("circle")  # circle = coin, triangle = dorito, square = sandwich/lettuce
goal.color("gold") # coin = gold, dorito = orange, sandwich = khaki, lettuce = green etc.
goal.penup()
goal.goto(250, -250) # Goal will be bottom right of screen

# Maze Walls Set Up.
walls = [] #empty array/list to store the wall object
wall_positions = [
    (-200, 200), (-200, 150), (-150, 150), (-150, 100),
    (-100, 100), (-100, 50), (-50, 50), (-50, 0),
    (0, 0), (0, -50), (50, -50), (50, -100),
    (100, -100), (100, -150), (150, -150), (150, -200)

] # Defines the coordinates of the walls

for pos in wall_positions :
    wall = turtle, turtle()
    wall.shape("square")
    wall.color("brown") # Wall Colour of your choice.
    wall.penup()
    wall.goto(pos) # Sets the position of the wall
    walls.append(wall) # Updates the wall object to the walls array.

# Player Movement

# Keyboard Events

# Main Game Loop
running = True
while running:
    screen.update() # Updates screen for updates
    time.sleep(0.05)   # Pause for 0.05 seconds to control game speed

    # Check for wall collision
    for wall in walls:
        if player.distance(wall) < 20:
            player.goto(-250, 250) # Sends player back to start.

    # Check if player reaches goal
    if player.distance(goal) < 20:
        print("You Win!")
        running = False # Ends game loop

screen.mainloop() # Keeps the window open until it's closed by the user.