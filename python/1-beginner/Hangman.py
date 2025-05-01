# Step 1: Import necessary libraries
import turtle  # Used for drawing the hangman
import random  # Used for selecting a random word
import sys  # Used for exiting the game


# Step 5: Define function to draw hangman based on remaining lives
def draw_hangman(lives):
    if lives == 5:
        # Draw the base and pole
        turtle.penup()
        turtle.setpos(-100, -200) 
        turtle.setheading(90)  # Point upwards
        turtle.pendown()
        turtle.forward(450)  # Vertical pole
        turtle.right(90)  # Rotate to draw top beam
        turtle.forward(100)  # Top beam
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
        turtle.forward(50)  # Body
        turtle.right(90)
        turtle.forward(50)  # Right arm
        turtle.backward(100)  # Left arm
        turtle.forward(50)
        turtle.left(90)
    elif lives == 1:
        # Draw one leg
        turtle.forward(100)
    elif lives == 0:
        # Draw the other leg and display 'Game Over'
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


# Step 6: Define function for ending the game and replaying
def game_finished(lives):
    play_again = input("Do you want to play again? [yes or no]: ")
    if play_again.lower() == "yes":
        print()
        if lives < 6:
            turtle.clear()  # Clear the screen for a new game
        play_hangman()
    else:
        print("Okay, thanks for playing!")
        sys.exit()


# Step 3: Define gameplay function
def play_hangman():
    # Select a random word from a file
    word = str(random.choice(open('words.txt').readlines())).strip()
    print("The word is " + str(len(word)) + " letters.\n")
    
    guesses = ""  # Store guessed letters
    lives = 6  # Player starts with 6 lives

    while lives > 0:
        print("Guess a letter:")
        guess = input()
        guesses += guess

        if guess not in word:
            # Wrong guess, lose a life and draw hangman
            lives -= 1
            draw_hangman(lives)
            print("Wrong")
            print("You have " + str(lives) + " lives left")

            if lives == 0:
                print("You Lose")
                print()
                game_finished(lives)

        failed = 0  # Count how many letters are missing
        
        if lives > 0:
            for char in word:
                if char in guesses:
                    print(char, end=" ")  # Show correct guesses
                else:
                    print("_", end=" ")  # Show blanks for unguessed letters
                    failed += 1
                    
            print("\n")

            if failed == 0:
                # If no blanks remain, player wins
                print("You won")
                print()
                game_finished(lives)  # Ask to replay


# Step 2: Welcome user & check if they want to play
play = input("Welcome to the HangMan HangOut! Do you have time for a game? [yes or no]: ")

if play.lower() == "yes":
    print()
    play_hangman()
else:
    print("Okay, have a good day!")
    sys.exit()