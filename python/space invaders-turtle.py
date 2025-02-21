import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Alien Invasion Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Player setup
player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()
player.goto(0, -250)

# Alien setup
alien = turtle.Turtle()
alien.shape("circle")
alien.color("red")
alien.penup()
alien.goto(random.randint(-200, 200), 250)

# Bullet setup
bullet = turtle.Turtle()
bullet.shape("square")
bullet.color("yellow")
bullet.penup()
bullet.shapesize(stretch_wid=0.5, stretch_len=1)
bullet.goto(0, -240)
bullet.hideturtle()

# Movement functions
def move_left():
    x = player.xcor()
    if x > -250:
        player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < 250:
        player.setx(x + 20)

def shoot():
    bullet.goto(player.xcor(), player.ycor() + 10)
    bullet.showturtle()
    move_bullet()

def move_bullet():
    y = bullet.ycor()
    while y < 300:
        y += 10
        bullet.sety(y)
        if abs(bullet.xcor() - alien.xcor()) < 20 and abs(bullet.ycor() - alien.ycor()) < 20:
            alien.goto(random.randint(-200, 200), 250)
            bullet.hideturtle()
            return
    bullet.hideturtle()

# Keyboard bindings
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(shoot, "space")

# Game loop
screen.mainloop()
