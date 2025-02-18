import time
import turtle

def setup_turtle():
    screen = turtle.Screen()
    screen.setup(300, 200)
    screen.title("Countdown Timer")
    
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0, 0)
    return t

def countdown(t, turtle_obj):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        turtle_obj.clear()
        turtle_obj.write(timer, align="center", font=("Arial", 36, "normal"))
        time.sleep(1)
        t -= 1
    
    turtle_obj.clear()
    turtle_obj.write("Time's up!", align="center", font=("Arial", 24, "normal"))
    
def get_time():
    while True:
        try:
            seconds = int(turtle.textinput("Countdown Timer", "Enter the time in seconds:"))
            if seconds > 0:
                return seconds
            else:
                turtle.textinput("Error", "Please enter a positive number.")
        except ValueError:
            turtle.textinput("Error", "Invalid input. Please enter a number.")

def main():
    turtle_obj = setup_turtle()
    seconds = get_time()
    countdown(seconds, turtle_obj)
    turtle.done()

if __name__ == '__main__':
    main()
