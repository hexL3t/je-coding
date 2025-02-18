import turtle
import random
import time

# Screen Set Up
# Set up the game window with a 400x400 size and a title
screen = turtle.Screen()
screen.setup(400,400)  # Width and height of the game screen
screen.title("Simple Snake Game")  # Title of the window
screen.tracer(0)  # Turns off automatic screen updates to allow for manual control of screen refresh

# Snake
# Creating the snake object and setting up its appearance
snake = turtle.Turtle()
snake.shape("square")  # The snake is a square
snake.color("green")  # Snake color is green
snake.penup()  # We don't want the snake to draw lines as it moves
snake.goto(0,0)  # Start the snake at the center of the screen
snake.direction = "stop"  # The snake starts with no movement

# Food
# Creating the food object that the snake will eat
food = turtle.Turtle()
food.shape("circle")  # The food is a circle
food.color("red")  # Food color is red
food.penup()  # Food also doesn't draw lines as it moves
food.goto(1, 100)  # Place the food at an initial random position

# Functions for controlling snake movement
# These functions change the direction of the snake
def go_up():
    if snake.direction != "down":  # Prevents the snake from going opposite to its current direction
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"
    
def go_left():
    if snake.direction != "right":
        snake.direction = "left"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"

# Move function to update the snake's position based on its current direction
def move():
    if snake.direction == "up":
        y = snake.ycor()  # Get the current y-coordinate
        snake.sety(y + 20)  # Move the snake upwards by 20 pixels
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)  # Move the snake downwards by 20 pixels
    if snake.direction == "left":
        x = snake.xcor()  # Get the current x-coordinate
        snake.setx(x - 20)  # Move the snake left by 20 pixels
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)  # Move the snake right by 20 pixels

# Keyboard bindings
# These allow the user to control the snake using the arrow keys
screen.listen()  # Tell the screen to listen for user inputs
screen.onkeypress(go_up, "Up")  # Bind the up arrow key to go_up function
screen.onkeypress(go_down, "Down")  # Bind the down arrow key to go_down function
screen.onkeypress(go_left, "Left")  # Bind the left arrow key to go_left function
screen.onkeypress(go_right, "Right")  # Bind the right arrow key to go_right function

# Main Game Loop
# This keeps the game running and constantly updates the screen
while True:
    screen.update()  # Manually update the screen to make it smooth
    
    # Check for collision with food
    if snake.distance(food) < 20:  # If the snake is close enough to the food
        x = random.randint(-180, 180)  # Generate a new random x position for the food
        y = random.randint(-180, 180)  # Generate a new random y position for the food
        food.goto(x, y)  # Move the food to the new random position
        
    move()  # Move the snake based on its current direction
    
    # Check for collision with walls
    if (snake.xcor() > 190 or snake.xcor() < -190 or
        snake.ycor() > 190 or snake.ycor() < -190):  # If the snake hits any of the screen boundaries
        snake.goto(0, 0)  # Reset the snake's position to the center
        snake.direction = "stop"  # Stop the snake's movement
        
    time.sleep(0.1)  # A small delay to control the speed of the game (the smaller the number, the faster the game)

# This keeps the window open after the main loop is finished
screen.mainloop()