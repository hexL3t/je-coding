import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Haunted Platformer")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off automatic updates

# Create player
player = turtle.Turtle()
player.shape("square")
player.color("orange")
player.penup()
player.speed(0)
player.goto(-350, -250)

# Player physics
player_speed = 20
player_dy = 0
gravity = -0.8
jump_force = 16
is_jumping = False

# Create platforms
platforms = []
platform_positions = [(-350, -270), (-150, -150), (100, -100), 
                     (-50, 0), (200, 50)]

for pos in platform_positions:
    platform = turtle.Turtle()
    platform.shape("square")
    platform.color("purple")
    platform.shapesize(stretch_wid=1, stretch_len=5)
    platform.penup()
    platform.goto(pos)
    platforms.append(platform)

# Create ghosts
ghosts = []
ghost_positions = [(0, -200), (150, -50), (-200, 100)]

for pos in ghost_positions:
    ghost = turtle.Turtle()
    ghost.shape("circle")
    ghost.color("white")
    ghost.penup()
    ghost.goto(pos)
    ghost.direction = 1  # 1 for right, -1 for left
    ghost.speed = 3
    ghosts.append(ghost)

# Score display
score_display = turtle.Turtle()
score_display.color("orange")
score_display.penup()
score_display.hideturtle()
score_display.goto(-380, 260)
score = 0

# Game over display
game_over_display = turtle.Turtle()
game_over_display.color("orange")
game_over_display.penup()
game_over_display.hideturtle()
game_over_display.goto(0, 0)

# Functions
def move_left():
    x = player.xcor()
    player.setx(x - player_speed)

def move_right():
    x = player.xcor()
    player.setx(x + player_speed)

def jump():
    global player_dy, is_jumping
    if not is_jumping:
        player_dy = jump_force
        is_jumping = True

def check_collision(t1, t2):
    distance = ((t1.xcor() - t2.xcor())**2 + 
                (t1.ycor() - t2.ycor())**2)**0.5
    return distance < 40

def reset_game():
    global score, game_over
    player.goto(-350, -250)
    score = 0
    game_over = False
    game_over_display.clear()
    
# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(jump, "space")
screen.onkey(reset_game, "r")

# Main game loop
game_over = False
while True:
    if not game_over:
        screen.update()
        
        # Apply gravity and update player position
        player_dy += gravity
        player.sety(player.ycor() + player_dy)
        
        # Platform collisions
        is_jumping = True
        for platform in platforms:
            if (player.ycor() - 20 <= platform.ycor() + 20 and
                player.ycor() - 10 >= platform.ycor() and
                abs(player.xcor() - platform.xcor()) < 50):
                player.sety(platform.ycor() + 20)
                player_dy = 0
                is_jumping = False
        
        # Screen boundaries
        if player.xcor() < -390:
            player.setx(-390)
        if player.xcor() > 380:
            player.setx(380)
        if player.ycor() < -290:
            player.sety(-290)
            player_dy = 0
            is_jumping = False
            
        # Move ghosts
        for ghost in ghosts:
            ghost.setx(ghost.xcor() + ghost.direction * ghost.speed)
            if ghost.xcor() > 380:
                ghost.direction = -1
            if ghost.xcor() < -390:
                ghost.direction = 1
                
            # Check for collision with ghost
            if check_collision(player, ghost):
                game_over = True
                game_over_display.write("Game Over! Press R to restart", 
                                      align="center", 
                                      font=("Arial", 24, "bold"))
        
        # Update score
        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", font=("Arial", 16, "normal"))
        
    time.sleep(1/60)  # Control game speed

screen.mainloop()