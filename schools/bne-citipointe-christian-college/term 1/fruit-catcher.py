#import libraries
import turtle
import random
import time

# Set Up Colour Mode
#turtle.colormode(255)

# Create the game screen
screen = turtle.Screen()
screen.bgcolor("alice blue") # Set background colour to a light colour
screen.setup(600, 800) # Set screen size (width, height)
#screen.title("Fruit Catcher")
screen.tracer(0) # Turn off automatic screen updates to optimise performance

# Create the score display
score_display = turtle.Turtle()
score_display.ht()  # Hide the turtle cursor from the screen
score_display.penup() # life the pen so no lines are drawn
score_display.goto(0, 350) # Move to the top of the screen to display score
score_display.color("white") # set score color to white

# Player's Basket
basket = turtle.Turtle()
basket.shape("square")   # Set shape to Square
basket.color("brown")     # Set colour of basket to a basket color (brown)
basket.shapesize(1, 4)    #Make the basket wider to catch more
basket.penup()
basket.goto(0, -300)      # Position Basket at bottom of screen

# Create arrays to store falling objects
fruits = []
bombs = []

# Global Game Variable
score = 0
game_over = False

# Set the speeed at which the basket moves
basket_speed = 20

# Flags to control continous movement
is_moving_left  = False
is_moving_right = False

# Functions to create new fruit falling from the top
def create_fruit():
    fruit = turtle.Turtle()
    fruit.shape("circle")       # Set fruit shape
    fruit.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))  # Assign a random color to the fruit
    fruit.penup()
    fruit.speed(0)
    fruit.goto(random.randint(-280, 280), 400)
    fruits.append(fruit) #Add fruit to the fruits list

# Function to create a new enemy (bomb) falling from the top
def create_bomb():
    bomb = turtle.Turtle()
    bomb.shape("circle")
    bomb.color("black")
    bomb.penup()
    bomb.speed(0)
    bomb.goto(random.randint(-280, 280), 400)
    bombs.append(bomb) # Add bomb to the bombs list

# Functions to control movement (continious)
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

# Functions for movement (click)
def move_left_click():
    x = basket.xcor()                   # Get current x-coordinates
    if  x > -280:                       # Ensure basket doesn't move past the left edge
        basket.setx(x + basket_speed)   # Move the basket left

def move_right_click():
    x = basket.xcor()                   # Get current x-coordinates
    if  x < 280:                       # Ensure basket doesn't move past the right edge
        basket.setx(x + basket_speed)   # Move the basket right

# Functions for movement (key)
def move_left_key():
    x = basket.xcor()                   # Get current x-coordinates
    if  x > -280:                       # Ensure basket doesn't move past the left edge
        basket.setx(x + basket_speed)   # Move the basket left

def move_right_key():
    x = basket.xcor()                   # Get current x-coordinates
    if  x < 280:                       # Ensure basket doesn't move past the right edge
        basket.setx(x + basket_speed)   # Move the basket right

# Set up keyboard bindings for multiple control options
screen.listen()  # Set up the screen to listen for user input
# Key controls (press and hold)
screen.onkeypress(start_move_left, "Left")   # Start moving left on arrow key press
screen.onkeypress(start_move_right, "Right")   # Start moving right on arrow key press
screen.onkeyrelease(stop_move_left, "Left")   # Start moving left on arrow key press
screen.onkeyrelease(stop_move_right, "Right")   # Start moving right on arrow key press

# Alternative 'A' and 'D' controls
screen.onkey(move_left_key, "a")  # Move left on 'A' key press
screen.onkey(move_right_key, "d")  # Move right on 'D' key press

# Mouse controls (click on screen)
screen.onkey(move_left_click, "1")  # Move left on clicking '1'
screen.onkey(move_right_click, "2")  # Move right on clicking '2'

# Main Loop
spawn_counter = 0 # initialise spawn counter to control spawn rate
while not game_over:
    screen.update() # Update the game after each loop
    time.sleep(0.016)  # control game speed

    # Hadndle Continious Movement
    if is_moving_left:
        move_left_key()  # Move the basket if the left key is being held
    if is_moving_right:
        move_right_key()    # Move the basket right if the right key is being held

# Spawn new objects periodicallyy
    spawn_counter += 1 # Increment the spawn counter
    if spawn_counter % 50 == 0:  # spawn every 50 frames

    # Update Score Display
    score_display.clear()
    
      # score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))
    score_display.write("Score: ", score) # Setting the Score