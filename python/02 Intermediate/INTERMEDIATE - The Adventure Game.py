# import libraries
import sys
import time
import random
from datetime import datetime as dt
# datetime is a class we will use within the datetime pkg FYI

# Declare a variable "game_items" equal to an empty dictionary
game_items = {}

# Declare a variable "name" equal to input with string:
name = input("Hello, please enter your name: ")

# Print a string to welcome player using the name they entered
print("Greetings and salutations, Adventurer " + name + "!")

# Now we are going to tell the player the current time
# (in case they have homework to finish!)
# strftime = string format time
print("The current time is: " + dt.now().strftime("%H:%M:%S %p") + ".")


# Create a function "setup_items"
def setup_items():
    # Declare "game_items" as global
    global game_items

    # Make "game_items" so that key "stick" is false & key "exhaust" is false
    game_items["stick"] = False
    game_items["exhaust"] = False


# Create a function called "game_over"
def game_over():
    # Create a variable called "restart" with value of input with string
    restart = input("Game Over! Want to try again? [yes or no]:\n")

    # Make a conditional statement to check the value of "restart"
    if restart == "yes":
        way()
    else:
        print("Thanks for playing!")
        sys.exit()


# Create a function called "tunnel"
def tunnel():
    print("You enter the next room. You realise it is a tunnel and see light "
          "at the end.\n")

    # Create a variable "decision" to gain value of input from string question
    decision = input("Will you run toward the light or inspect the room "
                     "further? [run or look]:\n")

    # Create an if condition to check if "decision" is "run"
    if decision == "run":
        print("Well, you almost made it to the end, but got killed by a huge "
              "log when you activated a trip-wire. That was incautious of you.\n")
        # Call "game_over" function
        game_over()

    # Make an elif condition to check if "decision" is "look"
    elif decision == "look":
        print("Good job, " + name + ", you noticed the trip-wire to avoid and "
              "made it out. Congratulations! You beat the game!!\n")
        # Call "game_over" function
        game_over()

    # Make an else statement to catch any other input
    else:
        # Call "game_over" function
        game_over()


# Create a function called "choice"
def choice():
    # Declare the variable "game_items" as global
    global game_items

    # Create a variable "decision" with value of input with string
    decision = input("You have the gold! You look around the room and see a "
                     "sword, which looks heavy, and another wooden door. If "
                     "you are to get the sword, you must drop the gold. So, you "
                     "must pick between the sword and gold [sword or gold]:\n")

    # Make a conditional statement to check if value of "decision" is "gold"
    if decision == "gold":

        # Create a variable "sneak" with value of input with string
        sneak = input("Ok, you pick wealth over a weapon. You walk through the "
                      "door and see a HUGE rat, it looks as though it is "
                      "sleeping. Sneak around it? [yes or no]:\n")

        # Make a conditional statement to check if "sneak" is "yes"
        if sneak == "yes":
            print("As you are sneaking, the gold bounces around in your "
                  "pocket...\n")

            # Create a random variable between 1 & 50
            chance = random.randint(1,50)

            # If the value of the "roll" is 25 or less
            if chance <= 25:
                is_awake = False
            else:
                is_awake = True

            if is_awake:
                print("Oh no! The noise from the coins woke the rat up! You "
                      "make a run for a door you glimpsed on the other side of "
                      "the chamber ...\n")

                # Create a new random variable to see if player ran fast enough
                fast_enough = random.randint(1, 20)

                # Check for value of fast_enough to see if player made it
                if fast_enough > 10:
                    print("Amazing! You must be track star! You sped past the "
                          "rat before it could get its teeth or claws on you.\n")

                    # Call next step in the adventure
                    tunnel()

                else:
                    print("Oh no! You just weren't fast enough. Those coins "
                          "must have weighed you down too much. You were rat "
                          "lunch.\n")

                    game_over()

            else:
                print("Lucky you! The rat did not wake up. You escaped through "
                      "a door on the other side of the chamber.\n")

                # Call next step in adventure
                tunnel()

        # Make an elif condition to check if "sneak" is "no"
        elif sneak == "no":
            print("The rat woke up and ate you, not the best choice.\n")
            # Call the "game_over" function
            game_over()

        # Make an else statement to catch any other input that is received
        else:
            game_over()

    # Make an elif condition to check if "decision" is "sword"
    elif decision == "sword":
        # Create a variable "rat" with value of input from string
        rat = input("You throw down the gold and pick up the sword. Then you "
                    "advance through a door, suddenly a large rat appears and "
                    "it looks angry. Will you run or fight? [run or fight]:\n")

        # Make an if condition to check if "rat" is "run"
        if rat == "run":

            # Create a variable to give player random chance to get past rat
            fast_enough = random.randint(1, 20)

            # Check for value of fast_enough to see if player made it
            if fast_enough > 10:
                print("Amazing! You must be track star! You sped past the rat "
                      "before it could get its teeth or claws on you.\n")

                # Call next step in the adventure
                tunnel()

            else:
                print("Oh no! You just weren't fast enough. You run as hard as "
                      "you can, but do not prevail. You were rat lunch.\n")

                # Call the "game_over" function
                game_over()

        # Make an elif condition to check if "rat" is "fight"
        elif rat == "fight":

            print("You attack the rat, hacking and slashing ...\n")

            # Create a variable to determine the random chance of the battle
            who_wins = random.randint(1, 8)

            # Check condition for who wins the battle
            if who_wins > 4:

                print("And you gain victory over the creature! Yay!!\n")

                # Call the next step in the adventure
                tunnel()

            else:

                print("The rat knocks the sword out of your hands and pins you "
                      "to the ground. You are doomed!\n")

                # Call the "game_over" function
                game_over()

        # Make else statement to catch any other input
        else:
            game_over()

    # Make an else statement to catch any other inputs
    else:
        # Call "game_over" function
        game_over()


# Create a function called "open_chest"
def open_chest():
    # Declare the variable "game_items" as global
    global game_items

    # Create a variable "have_item" with value of "game_items" key "exhaust"
    have_item = game_items["exhaust"]

    # Make a conditional statement to check if "have_item" is "True"
    if have_item:
        print("You attempt to pick them up, but keel over from exhaustion.\n")
        # Call the "game_over" function
        game_over()

    # Create variable called "have_stick" with value of "game_items" key "stick"
    have_stick = game_items["stick"]

    # Make a conditional statement to check if "have_stick" is "True"
    if have_stick:
        print("The chest was easier to open! You could carry the 40 gold "
              "pieces easily.\n")
        # Call next step in adventure
        choice()

    # Make a conditional statement to check if "have_stick" is "False"
    if not have_stick:
        print("You wait a little while to recover your strength... (5 "
              "seconds)\n")

        # Call the "time.sleep" function for 5 seconds
        time.sleep(5)

        # Call next step in adventure
        choice()


# Create a function called "chest"
def chest():
    # Declare variable "game_items" as global to update dictionary
    global game_items

    # Create a variable "decision" with value of input with string
    decision = input("You open the door and see a large chest. [open or look]:"
                     "\n")

    # Make a conditional statement to check if value of "decision" is "look"
    if decision == "look":
        # Create a variable stick with value of input with string
        stick = input("You see a stick that may give you leverage to open the "
                      "chest. Pick up stick? [yes or no]:\n")

        # Make a conditional statement to check the value of "stick"
        if stick == "yes":
            # Set "game_items" key "stick" to "True"
            game_items["stick"] = True
            # Call next step in adventure
            open_chest()
        else:  # Player said no to get stick, so game_items["stick"] = False
            # Call next step in adventure
            open_chest()

    # Make elif (else if) statement to check if value of "decision" is "open"
    elif decision == "open":
        # Create a variable "exhaust" with value of input with string
        exhaust = input("You barely get the chest open, you get exhausted from "
                        "the effort, but inside are at least 40 gold pieces. "
                        "They look heavy though. Will you pick up the pieces? "
                        "[yes or no]:\n")

        # Make an if condition to check if value of "exhaust" is "yes"
        if exhaust == "yes":
            # Set "game_items" key "exhaust" to "True"
            game_items["exhaust"] = True
            # Call next step in adventure
            open_chest()
        # Otherwise, use else to move forward
        else:
            # Call next step in adventure
            open_chest()


# Create a function called "try_door"
def try_door():
    decision = input("Now, to try the door? [yes or no]:\n")

    # Create a conditional statement to test the value of "decision"
    if decision == "no":
        around = input("Well, do you want to look around? [yes or no]:\n")

        # Make a conditional statement to check the value of "around"
        if around == "yes":
            print("There is nothing else here.\n")
            # Recall this function to make other choice
            try_door()
        # Otherwise, move forward in adventure
        else:
            # Call the next step in the adventure
            chest()

    # Otherwise, move forward in adventure
    else:
        # Call next step in adventure
        chest()


# Create a function called "cavern"
def cavern():
    # Create a variable "decision" with value of input with string
    decision = input("Will you try to hit the door, or climb the spring for "
                     "the key? [hit or climb]:\n")

    # Create an if condition to check if value of "decision" is "hit"
    if decision == "hit":
        print("You hit the door and got killed by a falling rock.\n")
        game_over()

    # Create an elif condition to check if value of "decision" is "climb"
    elif decision == "climb":
        print("Wow, you are a good climber, you got the key!\n")
        # Call next function in adventure
        try_door()

    # Create else statement for all other input
    else:
        game_over()


# Create a function called "way"
def way():
    # Create a variable "decision" with value of input with string
    decision = input("You are in a cave. There are two ways to go, which way "
                     "do you go? [left or right]:\n")

    # Create an condition to check if the value of "decision" is "left"
    if decision == "left":
        print("The door leads you into a small cavern with a spring in the "
              "centre and a key on the top, the key must lead to a small "
              "rotted door to the right of the spring.\n")
        # Call "cavern" function
        cavern()

    # Create an elif condition to check if the value of "decision" is "right"
    elif decision == "right":
        print("Sorry, you walked in and were killed by spikes.\n")
        game_over()

    # Create an else statement to catch all other input
    else:
        game_over()


# Function to start game & confirm player acquiescence
def start_game():
    # Call the "setup_items" function
    setup_items()

    # Declare a variable "play" with value of input with string
    play = input("Begin the game? [yes or no]: ")

    # Make a conditional statement to check value of "play" variable
    if play == "yes":
        print("Your adventure will commence!\n")
        way()
    # If player puts any value but "yes" then game will quit
    else:
        print("Okay, bye!\n")
        sys.exit()


# Call the function "start_game"
start_game()

print("\nThanks for playing!")