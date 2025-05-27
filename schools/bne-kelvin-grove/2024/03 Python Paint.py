import turtle

def setup_screen():
    screen = turtle.Screen()
    screen.setup(600, 400)
    screen.title("Advanced Drawing App")
    screen.bgcolor("white")
    return screen

def create_turtle():
    t = turtle.Turtle()
    t.pensize(3)
    t.speed(0)
    return t

def change_color(color):
    t.pencolor(color)

def toggle_pen():
    if t.isdown():
        t.penup()
    else:
        t.pendown()

def start_drawing(x, y):
    t.pendown()
    t.goto(x, y)

def draw(x, y):
    t.goto(x, y)

def erase(x, y):
    pen_color = t.pencolor()
    pen_size = t.pensize()
    t.pencolor("white")
    t.pensize(10)
    t.goto(x, y)
    t.pencolor(pen_color)
    t.pensize(pen_size)

def curve_left():
    t.circle(50, 45)

def curve_right():
    t.circle(-50, 45)

def clear_screen():
    t.clear()
    t.penup()
    t.home()

def main():
    global screen, t
    screen = setup_screen()
    t = create_turtle()

    color_keys = {
        'r': 'red', 'g': 'green', 'b': 'blue',
        'y': 'yellow', 'p': 'purple', 'o': 'orange', 'w': 'white'
    }

    # Create a turtle to display the color commands
    color_commands = turtle.Turtle()
    color_commands.penup()
    color_commands.goto(-280, -160)
    color_commands.write("Color Commands:", font=("Arial", 10, "bold"))
    color_commands.penup()
    color_commands.goto(-280, -180)

    # Display the color commands in a straight line
    for key, color in color_keys.items():
        screen.onkey(lambda c=color: change_color(c), key)
        color_commands.write(f"{key.upper()} : {color}", font=("Arial", 8))
        color_commands.setx(color_commands.xcor() + 80)

    color_commands.hideturtle()

    screen.onscreenclick(start_drawing, 1)
    screen.onscreenclick(lambda x, y: toggle_pen(), 3)
    screen.onkey(clear_screen, "space")
    screen.onkey(curve_left, "Left")
    screen.onkey(curve_right, "Right")
    screen.listen()

    t.ondrag(draw)

    # Set up eraser mode
    eraser_turtle = turtle.Turtle()
    eraser_turtle.hideturtle()
    eraser_turtle.penup()

    turtle.done()

if __name__ == "__main__":
    main()