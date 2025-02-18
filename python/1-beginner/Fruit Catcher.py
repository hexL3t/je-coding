import turtle
import random
import time

# Set up color mode for RGB values
turtle.colormode(255)

# Create the game screen
screen = turtle.Screen()
screen.bgcolor("skyblue")  # Set background color to sky blue
screen.setup(600, 800)  # Set screen size (width, height)
screen.title("Fruit Catcher")  # Set screen title
screen.tracer(0)  # Turn off automatic screen updates to optimize performance

# Create the score display turtle
score_display = turtle.Turtle()
score_display.hideturtle()  # Hide the turtle cursor from the screen
score_display.penup()  # Lift the pen so no lines are drawn
score_display.goto(0, 350)  # Move to the top of the screen to display score
score_display.color("white")  # Set score color to white

# Create the player's basket turtle
basket = turtle.Turtle()
basket.shape("square")  # Set basket shape to square
basket.color("brown")  # Set color of the basket to brown
basket.shapesize(1, 4)  # Make the basket wider to catch more fruits
basket.penup()  # Lift the pen so no lines are drawn
basket.goto(0, -300)  # Position the basket at the bottom of the screen

# Create lists to store falling objects (fruits and bombs)
fruits = []
bombs = []

# Initialize game variables
score = 0  # Initialize score to 0
game_over = False  # Flag to track if the game is over

# Set the speed at which the basket moves
basket_speed = 20

# Flags to control the continuous movement of the basket
is_moving_left = False
is_moving_right = False

# Function to create a new fruit falling from the top
def create_fruit():
    fruit = turtle.Turtle()
    fruit.shape("circle")  # Set fruit shape to a circle
    fruit.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Assign a random color to the fruit
    fruit.penup()  # Lift the pen so no lines are drawn
    fruit.speed(0)  # Set the fastest movement speed for the fruit
    fruit.goto(random.randint(-280, 280), 400)  # Set random starting position
    fruits.append(fruit)  # Add fruit to the fruits list

# Function to create a new bomb falling from the top
def create_bomb():
    bomb = turtle.Turtle()
    bomb.shape("circle")  # Set bomb shape to a circle
    bomb.color("black")  # Set color of the bomb to black
    bomb.penup()  # Lift the pen so no lines are drawn
    bomb.speed(0)  # Set the fastest movement speed for the bomb
    bomb.goto(random.randint(-280, 280), 400)  # Set random starting position
    bombs.append(bomb)  # Add bomb to the bombs list

# Functions to control the basket's movement
def start_move_left():
    global is_moving_left
    is_moving_left = True

def start_move_right():
    global is_moving_right
    is_moving_right = True

def stop_move_left():
    global is_moving_left
    is_moving_left = False

def stop_move_right():
    global is_moving_right
    is_moving_right = False

def move_left_click():
    x = basket.xcor()  # Get the current x-coordinate of the basket
    if x > -280:  # Ensure the basket doesn't move beyond the left edge
        basket.setx(x - basket_speed)  # Move the basket left

def move_right_click():
    x = basket.xcor()  # Get the current x-coordinate of the basket
    if x < 280:  # Ensure the basket doesn't move beyond the right edge
        basket.setx(x + basket_speed)  # Move the basket right

# Alternative controls using 'A' and 'D' keys
def move_left_key():
    x = basket.xcor()  # Get the current x-coordinate of the basket
    if x > -280:  # Ensure the basket doesn't move beyond the left edge
        basket.setx(x - basket_speed)  # Move the basket left

def move_right_key():
    x = basket.xcor()  # Get the current x-coordinate of the basket
    if x < 280:  # Ensure the basket doesn't move beyond the right edge
        basket.setx(x + basket_speed)  # Move the basket right

# Set up keyboard bindings for multiple control options
screen.listen()  # Set up the screen to listen for user input
# Arrow key controls (press and hold)
screen.onkeypress(start_move_left, "Left")  # Start moving left on arrow key press
screen.onkeypress(start_move_right, "Right")  # Start moving right on arrow key press
screen.onkeyrelease(stop_move_left, "Left")  # Stop moving left when the key is released
screen.onkeyrelease(stop_move_right, "Right")  # Stop moving right when the key is released

# Alternative 'A' and 'D' controls
screen.onkey(move_left_key, "a")  # Move left on 'A' key press
screen.onkey(move_right_key, "d")  # Move right on 'D' key press

# Mouse controls (click on screen)
screen.onkey(move_left_click, "1")  # Move left on clicking '1'
screen.onkey(move_right_click, "2")  # Move right on clicking '2'

# Display a debug message for controls
debug_display = turtle.Turtle()
debug_display.hideturtle()  # Hide the turtle cursor
debug_display.penup()  # Lift the pen so no lines are drawn
debug_display.goto(0, 300)  # Position the debug message near the top of the screen
debug_display.color("white")  # Set debug message color to white
debug_display.write("Controls: Arrow Keys, A/D keys, or 1/2 keys", align="center", font=("Arial", 12, "normal"))  # Show debug message

# Main game loop
spawn_counter = 0  # Initialize spawn counter to control spawning rate
while not game_over:  # Keep running the game until it's over
    screen.update()  # Update the screen after each loop iteration
    time.sleep(0.016)  # Control game speed by adding a small delay

    # Handle continuous movement
    if is_moving_left:
        move_left_key()  # Move the basket left if the left key is being held
    if is_moving_right:
        move_right_key()  # Move the basket right if the right key is being held

    # Spawn new objects periodically
    spawn_counter += 1  # Increment the spawn counter
    if spawn_counter % 50 == 0:  # Spawn every 50 frames
        if random.random() < 0.7:  # 70% chance for a fruit
            create_fruit()  # Create a new fruit
        else:  # 30% chance for a bomb
            create_bomb()  # Create a new bomb

    # Move fruits and check for collision and removal
    for fruit in fruits[:]:
        fruit.sety(fruit.ycor() - 5)  # Move fruit down

        # Check if the fruit has fallen within the basket's reach
        if (fruit.ycor() < -280 and fruit.ycor() > -320 and
            abs(fruit.xcor() - basket.xcor()) < 50):
            fruits.remove(fruit)  # Remove fruit from the list
            fruit.hideturtle()  # Hide the fruit from the screen
            score += 10  # Increase score for catching the fruit

        # Check if the fruit has fallen off the screen
        elif fruit.ycor() < -400:
            fruits.remove(fruit)  # Remove fruit from the list
            fruit.hideturtle()  # Hide the fruit from the screen

    # Move bombs and check for collision and removal
    for bomb in bombs[:]:
        bomb.sety(bomb.ycor() - 7)  # Move bomb down (bomb falls faster)

        # Check if the bomb has fallen into the basket
        if (bomb.ycor() < -280 and bomb.ycor() > -320 and
            abs(bomb.xcor() - basket.xcor()) < 50):
            game_over = True  # End the game if the bomb is caught

        # Check if the bomb has fallen off the screen
        elif bomb.ycor() < -400:
            bombs.remove(bomb)  # Remove bomb from the list
            bomb.hideturtle()  # Hide the bomb from the screen

    # Update the score display
    score_display.clear()  # Clear the previous score
    score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))  # Show the new score

# Game over display
score_display.goto(0, 0)  # Move to the center of the screen
score_display.write("GAME OVER!", align="center", font=("Arial", 36, "bold"))  # Display game over message

screen.mainloop()  # Keep the screen open until manually closed
