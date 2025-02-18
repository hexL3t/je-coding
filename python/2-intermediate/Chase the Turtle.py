import turtle
import random
import time

# Setup the game screen
screen = turtle.Screen()
screen.setup(400, 400)  # Set the window size to 400x400
screen.title("Catch the Turtle")  # Set the title of the window

# Create a turtle object to represent the target
t = turtle.Turtle()
t.shape("turtle")  # Set the turtle shape as a turtle icon
t.color("green")  # Set the turtle's color to green
t.penup()  # Lift the pen so it doesn't draw on the screen

# Initialize score and game_over status
score = 0
game_over = False

# Function to move the turtle to a random position on the screen
def move_turtle():
    t.goto(random.randint(-180, 180), random.randint(-180, 180))  # Randomly position the turtle

# Function to handle mouse clicks (on the turtle)
def on_click(x, y):
    global score, game_over
    if not game_over and t.distance(x, y) < 20:  # If the turtle is clicked and not game over
        score += 1  # Increase the score by 1
        move_turtle()  # Move the turtle to a new random position

# Set up the mouse click event listener
screen.onclick(on_click)

# Move the turtle to a random starting position
move_turtle()

# Start a timer to limit the game duration
start_time = time.time()

# Game loop: Run until the game is over
while not game_over:
    screen.update()  # Continuously update the screen
    if time.time() - start_time > 10:  # If the game duration exceeds 10 seconds
        game_over = True  # Set game_over to True to end the game

# When the game is over, hide the turtle and display the score
t.hideturtle()  # Hide the turtle icon
t.goto(0, 0)  # Move the turtle to the center of the screen
t.write(f"Game Over!", align="center", font=("Arial", 16, "normal"))  # Display "Game Over"
t.goto(0, -20)  # Move the turtle slightly down for the score
t.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))  # Display the final score

# Wait for a final click to close the game window
screen.exitonclick()