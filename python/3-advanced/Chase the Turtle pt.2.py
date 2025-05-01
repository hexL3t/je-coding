import turtle
import random
import time

# Setup the game screen
screen = turtle.Screen()
screen.setup(400, 400)  # Set screen size
screen.title("Catch the Turtle")  # Set the window title

# Create the turtle (player) that moves around the screen
t = turtle.Turtle()
t.shape("turtle")  # Set the turtle shape
t.color("green")  # Set the initial turtle color
t.penup()  # Lift the pen so the turtle doesn't draw lines

# Create a separate turtle for displaying the timer
timer = turtle.Turtle()
timer.hideturtle()  # Hide the timer turtle
timer.penup()  # Lift the pen so it doesn't draw
timer.goto(150, 150)  # Set the position of the timer

# Game variables
score = 0  # Initialize score
game_over = False  # Set the initial game state to not over
game_duration = 10  # Game duration in seconds

# Function to move the turtle to a random location on the screen
def move_turtle():
    t.goto(random.randint(-180, 180), random.randint(-180, 180))

# Function to change the turtle's color randomly
def change_color():
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    t.color(random.choice(colors))

# Function to handle clicks on the screen
def on_click(x, y):
    global score, game_over  # Access the global score and game_over variables
    # If the turtle is clicked and the game is not over
    if not game_over and t.distance(x, y) < 20:
        score += 1  # Increase the score by 1
        change_color()  # Change the turtle's color
        move_turtle()  # Move the turtle to a new random position

# Function to update the timer on the screen
def update_timer(time_left):
    timer.clear()  # Clear the previous timer text
    timer.write(f"Time: {time_left}", align="right", font=("Arial", 16, "normal"))

# Set the on_click function to be called when the screen is clicked
screen.onclick(on_click)

# Initial setup: move the turtle to a random position
move_turtle()

# Start the game timer
start_time = time.time()
last_second = game_duration  # Initialize last second as the full duration
update_timer(game_duration)  # Display the initial time

# Main game loop: runs until the game is over
while not game_over:
    screen.update()  # Update the screen
    time_elapsed = time.time() - start_time  # Calculate time passed since the game started
    current_second = max(0, game_duration - int(time_elapsed))  # Get the current second

    # Update the timer display if the second has changed
    if current_second != last_second:
        update_timer(current_second)
        last_second = current_second

    # If the time is up, end the game
    if time_elapsed > game_duration:
        game_over = True

# Hide the player turtle once the game is over
t.hideturtle()
timer.clear()  # Clear the timer

# Create another turtle to display the "Game Over" message and the final score
text_turtle = turtle.Turtle()
text_turtle.hideturtle()  # Hide the text turtle
text_turtle.penup()  # Lift the pen
text_turtle.color("black")  # Set the text color to black

# Display the "Game Over" message and score at the center of the screen
text_turtle.goto(0, 0)
text_turtle.write(f"Game Over!", align="center", font=("Arial", 16, "normal"))
text_turtle.goto(0, -20)
text_turtle.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

# Wait for the user to click to exit the game
screen.exitonclick()