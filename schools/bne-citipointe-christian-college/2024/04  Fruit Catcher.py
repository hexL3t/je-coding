import turtle
import random
import time

# Set up color mode for RGB values
turtle.colormode(255)

# Create the game screen
screen = turtle.Screen()
screen.bgcolor("skyblue")  # Set background color
screen.setup(600, 800)  # Set screen size
screen.title("Fruit Catcher")  # Set screen title
screen.tracer(0)  # Turn off automatic screen updates

# Create the score display
score_display = turtle.Turtle()
score_display.hideturtle()  # Hide the turtle cursor
score_display.penup()  # Pen up to prevent drawing lines
score_display.goto(0, 350)  # Set initial position
score_display.color("white")

# Create the player's basket
basket = turtle.Turtle()
basket.shape("square")  # Set shape to a square
basket.color("brown")  # Set color to brown
basket.shapesize(1, 4)  # Make the basket wider
basket.penup()
basket.goto(0, -300)  # Set initial position

# Create lists to store falling objects
fruits = []
bombs = []

# Initialize game variables
score = 0
game_over = False

# Set the speed of the basket's movement
basket_speed = 20

# Flags to control continuous movement
is_moving_left = False
is_moving_right = False

# Function to create a new fruit
def create_fruit():
    fruit = turtle.Turtle()
    fruit.shape("circle")
    fruit.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Random color
    fruit.penup()
    fruit.speed(0)
    fruit.goto(random.randint(-280, 280), 400)  # Random starting position
    fruits.append(fruit)

# Function to create a new bomb
def create_bomb():
    bomb = turtle.Turtle()
    bomb.shape("circle")
    bomb.color("black")
    bomb.penup()
    bomb.speed(0)
    bomb.goto(random.randint(-280, 280), 400)
    bombs.append(bomb)

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
    x = basket.xcor()
    if x > -280:
        basket.setx(x - basket_speed)

def move_right_click():
    x = basket.xcor()
    if x < 280:
        basket.setx(x + basket_speed)

# Alternative controls using 'A' and 'D' keys
def move_left_key():
    x = basket.xcor()
    if x > -280:
        basket.setx(x - basket_speed)

def move_right_key():
    x = basket.xcor()
    if x < 280:
        basket.setx(x + basket_speed)

# Set up keyboard bindings for multiple control options
screen.listen()
# Arrow key controls (press and hold)
screen.onkeypress(start_move_left, "Left")
screen.onkeypress(start_move_right, "Right")
screen.onkeyrelease(stop_move_left, "Left")
screen.onkeyrelease(stop_move_right, "Right")

# Alternative 'A' and 'D' controls
screen.onkey(move_left_key, "a")
screen.onkey(move_right_key, "d")

# Mouse controls (click on screen)
screen.onkey(move_left_click, "1")
screen.onkey(move_right_click, "2")

# Display a debug message
debug_display = turtle.Turtle()
debug_display.hideturtle()
debug_display.penup()
debug_display.goto(0, 300)
debug_display.color("white")
debug_display.write("Controls: Arrow Keys, A/D keys, or 1/2 keys", align="center", font=("Arial", 12, "normal"))

# Main game loop
spawn_counter = 0
while not game_over:
    screen.update()  # Update the screen
    time.sleep(0.016)  # Control game speed

    # Handle continuous movement
    if is_moving_left:
        move_left_key()
    if is_moving_right:
        move_right_key()

    # Spawn new objects periodically
    spawn_counter += 1
    if spawn_counter % 50 == 0:  # Spawn every 50 frames
        if random.random() < 0.7:  # 70% chance for fruit
            create_fruit()
        else:  # 30% chance for bomb
            create_bomb()

    # Move fruits and check for collision and removal
    for fruit in fruits[:]:
        fruit.sety(fruit.ycor() - 5)

        if (fruit.ycor() < -280 and fruit.ycor() > -320 and
            abs(fruit.xcor() - basket.xcor()) < 50):
            fruits.remove(fruit)
            fruit.hideturtle()
            score += 10

        elif fruit.ycor() < -400:
            fruits.remove(fruit)
            fruit.hideturtle()

    # Move bombs and check for collision and removal
    for bomb in bombs[:]:
        bomb.sety(bomb.ycor() - 7)  # Bombs fall faster

        if (bomb.ycor() < -280 and bomb.ycor() > -320 and
            abs(bomb.xcor() - basket.xcor()) < 50):
            game_over = True

        elif bomb.ycor() < -400:
            bombs.remove(bomb)
            bomb.hideturtle()

    # Update the score display
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))

# Game over display
score_display.goto(0, 0)
score_display.write("GAME OVER!", align="center", font=("Arial", 36, "bold"))

screen.mainloop()