# Turtle Jump
# import libraries
import turtle
import random
import time

# Screen Set Up
screen = turtle.Screen()
screen.tracer(0,0)
screen.setup(500,500)
screen.title("Turtle Jump")
turtle.hideturtle()

# Player turtle and horizontal buttons
player = turtle.Turtle()
player.penup()
player.shape("turtle")
player.seth(90)
player.goto(0,-50)

# Setting up Variables
pX = 0
pY = 0
gravity = 1
jumping = False
platforms = []
platSize = 10

# Platform to Platform
firstPlat = turtle.Turtle()
firstPlat.penup()
firstPlat.shape("square")
firstPlat.shapesize(0.5, platSize)
firstPlat.goto(0,-100)
platforms.append(firstPlat)

# Define a Function
def new_plat():
    global platSize
    if platSize > 5:
        platSize -= 0.1
    prevPlat = platforms[-1].ycor()
    newPlat = turtle.Turtle()
    newPlat.penup()
    newPlat.shape("square")
    newPlat.shapesize(0.5, platSize)
    newPlat.color((random.uniform(0,1), random.uniform(0,1), random.uniform(0,1)))
    newPlat.goto(random.randint(-200, 200), prevPlat + 105)
    platforms.append(newPlat)
    
# Turtle Movement
def go_left():
    global pX
    if not pX > 0:
        pX = -10

def go_right():
    global pX
    if not pX < 0:
        pX = 10
        
def stop_left():
    global pX
    if not pX > 0:
        pX = 0
        
def stop_right():
    global pX
    if not pX < 0:
        pX = 0
        
def jump():
    global pY, jumping
    if not jumping:
        pY = 17
        jumping = True
        
screen.listen()
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")
screen.onkeypress(jump, "Up")
screen.onkeyrelease(stop_left, "Left")
screen.onkeyrelease(stop_right, "Right")

for _ in range(5):
    new_plat()
    
#Main Loop
while True:
    player.setx(player.xcor() + pX)
    if player.xcor() < -230 and pX < 0:
        player.setx(-230)
    elif player.xcor() > 230 and pX > 0:
        player.setx(230)
        
    pY -= gravity
    for plat in platforms:
        size = plat.shapesize()
        if (player.xcor() >= plat.xcor() - size[1] * 10 and player.xcor() <= plat.xcor() + size[1] * 10) and (player.ycor() <= plat.ycor() + 10 and player.ycor() >= plat.ycor() - 10) and pY < 0:
                player.sety(plat.ycor() + 10)
                pY = 0
                jumping = False
                
    player.sety(player.ycor() + pY)
    if player.ycor() > 0:
        scroll = player.ycor()
        player.sety(0)
        for plat in range(len(platforms)):
            platforms[plat].sety(platforms[plat].ycor() - scroll)
    
    for plat in range(len(platforms)-1, -1,-1):
        if platforms[plat].ycor() < -250:
            platforms.pop(plat)
            new_plat()
            
    time.sleep(0.02)
    screen.update()