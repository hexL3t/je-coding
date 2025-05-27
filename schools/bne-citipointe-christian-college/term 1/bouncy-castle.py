import turtle
import random
import time

# ---  Screen Set Up ---
# Setup the screen with an appropriate size and name.
screen = turtle.Screen()
screen.tracer(0,0)  # Tracer is tracking of movements, 0 = none
screen.setup(500,500)
screen.title("Bouncing Castle")
turtle.hideturtle()

# -- Turtle Storage --
# All information for turtles are stored in these lists.
bouncers = [] #contains all turtle objects, will be used for their x-y coordinates
bDX = [] # bDX and bDY are the "change" speeds for each turtle.
bDY = []
jumpHeights = [] # jumpHeights are the height that each turtle will bounce at.

# -- Global Variables ---
# Simple adjustable variables for this program. Feel free to adjust.
n = 20  # n is the number of turtles you want to have bouncing on screen.
gravity = 1

# --- Turtle Creation ---
# For as many as n, create a turtle with random colours and properties.
# Each turtle will have a random DX, a DY and jumpHeight to match when added to the list.
for _ in range(n):
    turt = turtle.Turtle()
    turt.color((random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)))
    turt.shape("turtle")
    turt.seth(90)
    turt.penup()
    bouncers.append(turt)
    bDX.append(random.randint(-5,5))
    bDY.append(0)
    jumpHeights.append(random.randint(10,30))

# -- Main Loop --
# No interactivity. Just want them bounce for as long as you want.
while True:
    # For each turtle, check X- boundaries, bounce or or add gravity to DY and move the turtle.
    for b in range(len(bouncers)):
        # Doubling up on both the boundary and DX speeds, it prevents a turtle from going out of bounds.
        if (bouncers[b].xcor() < -230 and bDX[b] < 0) or (bouncers[b].xcor() > 230 and bDX[b] > 0):
            bDX[b] *= -1

        # Check if the turtle has reached the bottom of the screen. Bounce them back up if they do
        #   by setting the DY to jumpHeight.
        # Else, add gravity to DY.
        if bouncers[b].ycor() < -230 and bDY[b] < 0:
            bDY[b] = jumpHeights[b]
        else:
            bDY[b] -= gravity
        # Move each turtle to their new position by adding DX and DY to x-y coordinates, respectively.
        bouncers[b].setx(bouncers[b].xcor() + bDX[b])
        bouncers[b].sety(bouncers[b].ycor() + bDY[b])
    
    # Sleep for a bit to slow down the program.
    time.sleep(0.02)
    # Update the screen.
    screen.update()
