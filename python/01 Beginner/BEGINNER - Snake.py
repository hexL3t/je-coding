import turtle
import random
import time

# Screen Set Up
screen = turtle.Screen()
screen.setup(400,400)
screen.title("Simple Snake Game")
screen.tracer(0)

# Snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(1, 100)

# Functions
def go_up():
    if snake.direction != "down":
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

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Main Game Loop
while True:
    screen.update()
    
    # Check for collision with food
    if snake.distance(food) < 20:
        x = random.randint(-180, 180)
        y = random.randint(-180, 180)
        food.goto(x,y)
        
    move()
    
    # Check for collision with walls
    if (snake.xcor() > 190 or snake.xcor() < -190 or
        snake.ycor() > 190 or snake.ycor() < -190):
        snake.goto(0,0)
        snake.direction = "stop"
        
    time.sleep(0.1) # A small delay to control game speed

screen.mainloop()