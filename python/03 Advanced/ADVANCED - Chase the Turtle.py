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

timer = turtle.Turtle()
timer.hideturtle()
timer.penup()
timer.goto(150, 150)

score = 0
game_over = False
game_duration = 10  # 10 seconds game duration

def move_turtle():
    t.goto(random.randint(-180, 180), random.randint(-180, 180))

def change_color():
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    t.color(random.choice(colors))

def on_click(x, y):
    global score, game_over
    if not game_over and t.distance(x, y) < 20:
        score += 1
        change_color()
        move_turtle()

def update_timer(time_left):
    timer.clear()
    timer.write(f"Time: {time_left}", align="right", font=("Arial", 16, "normal"))

screen.onclick(on_click)
move_turtle()

start_time = time.time()
last_second = game_duration
update_timer(game_duration)

while not game_over:
    screen.update()
    time_elapsed = time.time() - start_time
    current_second = max(0, game_duration - int(time_elapsed))
    
    if current_second != last_second:
        update_timer(current_second)
        last_second = current_second
    
    if time_elapsed > game_duration:
        game_over = True

t.hideturtle()
timer.clear()

text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.color("black")

text_turtle.goto(0, 0)
text_turtle.write(f"Game Over!", align="center", font=("Arial", 16, "normal"))
text_turtle.goto(0, -20)
text_turtle.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

screen.exitonclick()