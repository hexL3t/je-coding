# Import Libraries
import turtle
import random
import sys

# Define function to draw hangman based on remaining lives
def draw_hangman(lives):
    if lives == 5:
        # Draw the base and pole
        turtle.penup()
        turtle.setpos(-100, -200)
        turtle.setheading(90)
        turtle.pendown()
        turtle.forward(450)     # Vertical Pole
        turtle.right(90)        # Rotate to draw top beam
        turtle.forward(100)     # Top Beam
    elif lives == 4:
        # Draw the hanging rope
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
    elif lives == 3:
        # Draw the head
        turtle.circle(50)
        turtle.left(90)
    elif lives == 2:
        # Draw the body and one arm
        turtle.penup()
        turtle.forward(100)
        turtle.pendown()
        turtle.forward(50) # Body
        turtle.right(90)
        turtle.forward(50) # Right Arm
        turtle.backward(100) #Left Arm
        turtle.forward(50)
        turtle.left(90)
    elif lives == 1:
        # Draw One leg
        turtle.forward(100)
    elif lives == 0:
        # draw the other leg and display game over
        turtle.left(45)
        turtle.forward(75)
        turtle.backward(75)
        turtle.right(90)
        turtle.forward(75)
        turtle.left(135)
        turtle.penup() 
        turtle.setpos(0, 0)  # Move to center
        turtle.pendown() 
        turtle.write("Game Over", align="center", font=("Comic Sans MS", 20, "bold"))

# Define function for ending the game and replaying
def game_finished(lives):
    play_again = input("Do you want to play again? [yes/no]: ")
    if play_again.lower() == "yes":
        print()
        if lives < 6:
            turtle.clear() # clear the screen for a new game
            play_hangman()
        else: 
            print("Okay, thanks for playing!")
            sys.exit() # Comment out if needed (trinket.io)

# Define gameplay function
def play_hangman():
    # Select a random word from a file
    word = str(random.choice(open('words.txt').readlines())).strip()
    print("The word is " + str(len(word)) + " letters.\n")
    guesses = ""    # Store guessed letters
    lives = 6       # Player starts with 6 lives
    while lives > 0:
        print("Guess a letter: ")
        guess = input()
        guesses += guess
        #If guess is wrong, loose a life and draw hangman
        if guess not in word:
            lives -= 1  # lives = lives - 1
            draw_hangman(lives)
            print("Wrong.")
            print("You have " + str(lives) + " lives left")

            if lives == 0:
                print("You Lose.\n")
                game_finished(lives)
        
        failed = 0 # Count how many letters are missing

        if lives > 0:
            for char in word:
                if char in guesses:
                    print("_")
                    # print(char, end=" ") # Show the correct guesses
                else:
                    print("_")
                    # print("_", end=" ") # Show blanks for unguesses letters
                    failed += 1
            
            print("\n")  # Empty new line

            if failed == 0:
                # if no blanks remain, player wins
                print("You Won!\n")
                game_finished(lives)

# Welcome User & Check to Play
play = input("Welcome to the HangMan HangOut!\n"
             "Do you have time for a game?\n"
             "[yes or no]")

if play == "yes":
    play_hangman()
else:
    print("Okay, have a good day!")
    sys.exit()