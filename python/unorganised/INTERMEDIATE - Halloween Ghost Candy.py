import turtle
import random
import math
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Ghost's Halloween Adventure")
screen.setup(800, 600)
screen.tracer(0)  # Turn off animation for smooth movement

# Create the ghost (player)
ghost = turtle.Turtle()
ghost.penup()
ghost.color("white")
ghost.shape("circle")
ghost.speed(0)
ghost_speed = 1

# Movement state variables
movement = {
    'up': False,
    'down': False,
    'left': False,
    'right': False
}

# Create candy pieces
candies = []
for _ in range(5):
    candy = turtle.Turtle()
    candy.penup()
    candy.color("pink")
    candy.shape("triangle")
    candy.speed(0)
    x = random.randint(-350, 350)
    y = random.randint(-250, 250)
    candy.goto(x, y)
    candies.append(candy)

# Create jack-o'-lanterns (obstacles)
pumpkins = []
for _ in range(3):
    pumpkin = turtle.Turtle()
    pumpkin.penup()
    pumpkin.color("orange")
    pumpkin.shape("circle")
    pumpkin.speed(0)
    x = random.randint(-350, 350)
    y = random.randint(-250, 250)
    pumpkin.goto(x, y)
    pumpkin.dx = random.randint(-3, 3)
    pumpkin.dy = random.randint(-3, 3)
    pumpkins.append(pumpkin)

# Score display
score_display = turtle.Turtle()
score_display.penup()
score_display.color("white")
score_display.hideturtle()
score_display.goto(0, 260)
score = 0

# Timer display
timer_display = turtle.Turtle()
timer_display.penup()
timer_display.color("white")
timer_display.hideturtle()
timer_display.goto(300, 260)

# Movement functions
def start_up():
    movement['up'] = True

def start_down():
    movement['down'] = True

def start_left():
    movement['left'] = True

def start_right():
    movement['right'] = True

def stop_up():
    movement['up'] = False

def stop_down():
    movement['down'] = False

def stop_left():
    movement['left'] = False

def stop_right():
    movement['right'] = False

# Move ghost based on current movement state
def move_ghost():
    x = ghost.xcor()
    y = ghost.ycor()
    
    if movement['up'] and y < 280:
        ghost.sety(y + ghost_speed)
    if movement['down'] and y > -280:
        ghost.sety(y - ghost_speed)
    if movement['left'] and x > -380:
        ghost.setx(x - ghost_speed)
    if movement['right'] and x < 380:
        ghost.setx(x + ghost_speed)

# Keyboard bindings
screen.listen()
# Key press events
screen.onkeypress(start_up, "Up")
screen.onkeypress(start_down, "Down")
screen.onkeypress(start_left, "Left")
screen.onkeypress(start_right, "Right")
# Key release events
screen.onkeyrelease(stop_up, "Up")
screen.onkeyrelease(stop_down, "Down")
screen.onkeyrelease(stop_left, "Left")
screen.onkeyrelease(stop_right, "Right")

# Function to check collision
def is_collision(t1, t2):
    distance = math.sqrt((t1.xcor() - t2.xcor())**2 + (t1.ycor() - t2.ycor())**2)
    return distance < 20

# Main game loop
start_time = time.time()
game_duration = 45  # 45 seconds
game_active = True

while game_active:
    screen.update()
    
    # Handle continuous movement
    move_ghost()
    
    # Update timer
    elapsed_time = int(time.time() - start_time)
    remaining_time = game_duration - elapsed_time
    timer_display.clear()
    timer_display.write(f"Time: {remaining_time}s", align="center", font=("Arial", 16, "normal"))
    
    if remaining_time <= 0:
        game_active = False
        break
    
    # Move pumpkins
    for pumpkin in pumpkins:
        x = pumpkin.xcor() + pumpkin.dx
        y = pumpkin.ycor() + pumpkin.dy
        
        # Bounce off walls
        if x > 380 or x < -380:
            pumpkin.dx *= -1
        if y > 280 or y < -280:
            pumpkin.dy *= -1
            
        pumpkin.goto(x, y)
        
        # Check collision with ghost
        if is_collision(ghost, pumpkin):
            ghost.goto(0, 0)  # Reset ghost position
            score -= 5
            score_display.clear()
            score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))
    
    # Check candy collection
    for candy in candies[:]:
        if is_collision(ghost, candy):
            candy.goto(random.randint(-350, 350), random.randint(-250, 250))
            score += 10
            score_display.clear()
            score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

# Game over
screen.clear()
screen.bgcolor("black")
final_score = turtle.Turtle()
final_score.penup()
final_score.color("white")
final_score.hideturtle()
final_score.write(f"Game Over!\nFinal Score: {score}", align="center", font=("Arial", 24, "normal"))

screen.exitonclick()