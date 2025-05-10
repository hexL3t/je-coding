import random  # Import the random module for word selection and shuffling

# Step 1: Create a list of words to use in the game
word_list = ['python', 'coding', 'programming', 'debug', 'function', 'variable']

# Step 2: Define a function that scrambles the letters of a word
def scramble_word(word):
    word_letters = list(word)  # Convert the word into a list of characters
    random.shuffle(word_letters)  # Randomly rearrange the characters
    return ''.join(word_letters)  # Join the characters back into a string

# Step 3: Define the game logic in a function
def play_game():
    word = random.choice(word_list)  # Randomly pick a word from the list
    scrambled = scramble_word(word)  # Scramble the word
    print(f"\n🔤 Unscramble this word: {scrambled}")  # Show scrambled word

    attempts = 0  # Keep track of how many guesses the user makes

    while True:  # Loop until the correct guess is made
        guess = input("Your guess: ").lower()  # Get user input and convert to lowercase
        attempts += 1  # Count the attempt

        if guess == word:
            # Correct guess
            print(f"✅ Correct! You got it in {attempts} attempt(s).\n")
            break  # Exit the loop
        else:
            # Incorrect guess
            print("❌ Incorrect. Try again.")

# Step 4: Main function to manage replaying the game
def main():
    print("🎮 Welcome to the Word Scramble Game!")

    while True:  # Loop to allow multiple rounds
        play_game()  # Run one round
        again = input("Play again? (y/n): ").lower()  # Ask if player wants to continue
        if again != 'y':  # Exit if not 'y'
            print("Thanks for playing!")
            break  # End the game

# Step 5: Start the game
main()
