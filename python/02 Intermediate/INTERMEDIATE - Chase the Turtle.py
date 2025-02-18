import turtle
import random
import time

screen = turtle.Screen()
screen.setup(400, 400)
screen.title("Catch the Turtle")

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()

score = 0
game_over = False

def move_turtle():
    t.goto(random.randint(-180, 180), random.randint(-180, 180))

def on_click(x, y):
    global score, game_over
    if not game_over and t.distance(x, y) < 20:
        score += 1
        move_turtle()

screen.onclick(on_click)
move_turtle()

start_time = time.time()
while not game_over:
    screen.update()
    if time.time() - start_time > 10:  # 30 seconds game duration
        game_over = True

t.hideturtle()
t.goto(0,0)
t.write(f"Game Over!", align="center", font=("Arial", 16, "normal"))
t.goto(0,-20)
t.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))
screen.exitonclick()