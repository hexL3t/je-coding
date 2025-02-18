import turtle
import random
import math
import time

# Set up screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Haunted Maze Maker")
screen.setup(800, 600)
screen.tracer(0)

# Create player (maze builder)
player = turtle.Turtle()
player.shape("square")
player.color("purple")
player.penup()
player.speed(0)
player_speed = 1

# Create ghost (chaser)
ghost = turtle.Turtle()
ghost.shape("circle")
ghost.color("white")
ghost.penup()
ghost.speed(0)
ghost.goto(-350, 250)  # Start in top-left corner
ghost_speed = 0.2

# Create wall placer (follows player)
wall_placer = turtle.Turtle()
wall_placer.shape("square")
wall_placer.color("orange")
wall_placer.penup()
wall_placer.speed(0)

# Create walls list and wall builder state
walls = []
building_walls = False

# Score and time display
display = turtle.Turtle()
display.color("white")
display.penup()
display.hideturtle()
display.goto(0, 260)

# Movement state
movement = {
    'up': False,
    'down': False,
    'left': False,
    'right': False
}

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

# Wall building functions
def start_building(x, y):
    global building_walls
    building_walls = True

def stop_building(x, y):
    global building_walls
    building_walls = False

def create_wall():
    if len(walls) < 50:  # Limit total walls
        wall = turtle.Turtle()
        wall.shape("square")
        wall.color("brown")
        wall.penup()
        wall.speed(0)
        wall.goto(wall_placer.xcor(), wall_placer.ycor())
        walls.append(wall)

# Move player based on current movement state
def move_player():
    x = player.xcor()
    y = player.ycor()
    
    if movement['up'] and y < 280:
        player.sety(y + player_speed)
    if movement['down'] and y > -280:
        player.sety(y - player_speed)
    if movement['left'] and x > -380:
        player.setx(x - player_speed)
    if movement['right'] and x < 380:
        player.setx(x + player_speed)
        
    # Update wall placer position to follow player
    wall_placer.goto(player.xcor(), player.ycor())

def move_ghost_towards_player():
    # Calculate direction to player
    angle = math.atan2(player.ycor() - ghost.ycor(), 
                      player.xcor() - ghost.xcor())
    
    # Try to move towards player while avoiding walls
    new_x = ghost.xcor() + ghost_speed * math.cos(angle)
    new_y = ghost.ycor() + ghost_speed * math.sin(angle)
    
    # Check for wall collisions
    can_move = True
    for wall in walls:
        if math.sqrt((new_x - wall.xcor())**2 + (new_y - wall.ycor())**2) < 20:
            can_move = False
            break
    
    if can_move:
        ghost.goto(new_x, new_y)
    else:
        # Try to move in a random direction if blocked
        angle = random.uniform(0, 2 * math.pi)
        ghost.goto(ghost.xcor() + ghost_speed * math.cos(angle),
                  ghost.ycor() + ghost_speed * math.sin(angle))

# Set up keyboard bindings
screen.listen()
screen.onkeypress(start_up, "Up")
screen.onkeypress(start_down, "Down")
screen.onkeypress(start_left, "Left")
screen.onkeypress(start_right, "Right")
screen.onkeyrelease(stop_up, "Up")
screen.onkeyrelease(stop_down, "Down")
screen.onkeyrelease(stop_left, "Left")
screen.onkeyrelease(stop_right, "Right")

# Set up mouse bindings for wall building
screen.onscreenclick(start_building, 1)  # Left click
screen.onscreenclick(stop_building, 3)   # Right click

# Initialize game variables
score = 0
start_time = time.time()
game_duration = 60  # 60 seconds
last_wall_time = 0
wall_cooldown = 0.5  # Half second cooldown between wall placements

# Game instructions
instructions = turtle.Turtle()
instructions.color("white")
instructions.penup()
instructions.hideturtle()
instructions.goto(0, 0)
instructions.write("Build walls with left-click (hold)\nAvoid the ghost!\nRight-click to stop building\nPress any arrow key to start",
                  align="center", font=("Arial", 16, "normal"))
instructions.clear()

# Main game loop
game_active = True

while game_active:
    screen.update()
    
    # Update timer and score
    elapsed_time = int(time.time() - start_time)
    remaining_time = game_duration - elapsed_time
    display.clear()
    display.write(f"Time: {remaining_time}s | Score: {score} | Walls: {len(walls)}/50",
                 align="center", font=("Arial", 16, "normal"))
    
    if remaining_time <= 0:
        game_active = False
        break
    
    # Move player
    move_player()
    
    # Build walls if active and cooldown has passed
    if building_walls and time.time() - last_wall_time > wall_cooldown:
        create_wall()
        last_wall_time = time.time()
        score += 1
    
    # Move ghost
    move_ghost_towards_player()
    
    # Check for ghost catching player
    if math.sqrt((player.xcor() - ghost.xcor())**2 + 
                 (player.ycor() - ghost.ycor())**2) < 20:
        game_active = False
        break

# Game over screen
screen.clear()
screen.bgcolor("black")
final_display = turtle.Turtle()
final_display.color("white")
final_display.penup()
final_display.hideturtle()
if remaining_time <= 0:
    message = "You survived!"
else:
    message = "The ghost caught you!"
final_display.write(f"Game Over!\n{message}\nFinal Score: {score}",
                   align="center", font=("Arial", 24, "normal"))

screen.exitonclick()