import turtle
import random
import time

# Screen setup
# This sets up the window where the game will be displayed.
screen = turtle.Screen()
screen.setup(400, 400)  # Screen size (width, height)
screen.title("Simple Snake Game")  # Title of the window
screen.tracer(0)  # Turns off automatic screen updates for smooth manual updates

# Snake
# Create the snake's head using the Turtle module
snake = turtle.Turtle()
snake.shape("square")  # Snake head is represented by a square
snake.color("green")  # Snake color is green
snake.penup()  # Disable drawing lines as the snake moves
snake.goto(0, 0)  # Position the snake in the center of the screen
snake.direction = "stop"  # The snake starts in a "stopped" state (not moving)

# Snake body
# A list that will hold the snake's body segments as it grows
segments = []

# Food
# Create the food object using the Turtle module
food = turtle.Turtle()
food.shape("circle")  # Food is represented as a circle
food.color("red")  # Food color is red
food.penup()  # Disable drawing lines as the food moves
food.goto(0, 100)  # Place the food at a random position (initially at (0, 100))

# Functions for controlling snake movement
def go_up():
    if snake.direction != "down":  # Prevent the snake from moving opposite to its current direction
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

# Move function to update the snake's position based on its direction
def move():
    # Move the body segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()  # Get the x coordinate of the previous segment
        y = segments[index-1].ycor()  # Get the y coordinate of the previous segment
        segments[index].goto(x, y)  # Move the segment to the previous segment's position
    
    # Move the first body segment to the position of the snake's head
    if len(segments) > 0:  # Check if there are any segments
        x = snake.xcor()  # Get the x coordinate of the snake's head
        y = snake.ycor()  # Get the y coordinate of the snake's head
        segments[0].goto(x, y)  # Move the first segment to the head's position
        
    # Move the snake's head based on its direction
    if snake.direction == "up":
        snake.sety(snake.ycor() + 20)  # Move the head up by 20 pixels
    if snake.direction == "down":
        snake.sety(snake.ycor() - 20)  # Move the head down by 20 pixels
    if snake.direction == "left":
        snake.setx(snake.xcor() - 20)  # Move the head left by 20 pixels
    if snake.direction == "right":
        snake.setx(snake.xcor() + 20)  # Move the head right by 20 pixels

# Keyboard bindings
# Allow the player to control the snake using the arrow keys
screen.listen()  # Begin listening for keypress events
screen.onkeypress(go_up, "Up")  # Bind the Up arrow key to the go_up function
screen.onkeypress(go_down, "Down")  # Bind the Down arrow key to the go_down function
screen.onkeypress(go_left, "Left")  # Bind the Left arrow key to the go_left function
screen.onkeypress(go_right, "Right")  # Bind the Right arrow key to the go_right function

# Main game loop
# Keeps the game running and updates the screen
while True:
    screen.update()  # Manually update the screen after every iteration
    
    # Check for collision with food
    if snake.distance(food) < 20:  # Check if the snake's head is close to the food
        # Move the food to a random position
        x = random.randint(-180, 180)  # Random x coordinate
        y = random.randint(-180, 180)  # Random y coordinate
        food.goto(x, y)  # Place the food at the new random position
        
        # Add a new segment to the snake's body
        new_segment = turtle.Turtle()
        new_segment.shape("square")  # The new segment is a square
        new_segment.color("green")  # The new segment is green
        new_segment.penup()  # The new segment doesn't draw lines as it moves
        segments.append(new_segment)  # Add the new segment to the list of segments
    
    move()  # Move the snake based on its current direction
    
    # Check for collision with the wall (screen boundaries)
    if (snake.xcor() > 190 or snake.xcor() < -190 or 
        snake.ycor() > 190 or snake.ycor() < -190):  # If the snake hits a wall
        snake.goto(0, 0)  # Reset the snake's position to the center
        snake.direction = "stop"  # Stop the snake's movement
        
        # Hide all the segments by moving them off-screen
        for segment in segments:
            segment.goto(1000, 1000)  # Move each segment far off-screen
        
        # Clear the segments list so the snake can be reset
        segments.clear()
    
    time.sleep(0.1)  # Add a short delay to control the game speed

# Keep the game window open after the loop finishes
screen.mainloop()