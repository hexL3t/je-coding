import random  # Used to randomly select and shuffle words
import time    # Used to track how long it takes the player

# Step 1: List of words the player can guess
word_list = ['python', 'coding', 'programming', 'debug', 'function', 'variable']

# Step 2: Global scoreboard variables to track best performance across rounds
best_attempts = None  # Will store the fewest attempts it took to solve a word
best_time = None      # Will store the fastest time it took

# Step 3: Scramble a word by shuffling its letters
def scramble_word(word):
    word_letters = list(word)         # Convert word to list of characters
    random.shuffle(word_letters)      # Shuffle the characters
    return ''.join(word_letters)      # Rejoin into a scrambled string

# Step 4: Main game logic
def play_game():
    global best_attempts, best_time  # Use global variables to update scoreboard

    word = random.choice(word_list)  # Select a random word
    scrambled = scramble_word(word)  # Scramble it
    print(f"\n🔤 Unscramble this word: {scrambled}")

    attempts = 0         # Count number of user guesses
    hint_used = False    # Allow only one hint per game
    start_time = time.time()  # Start the timer

    while True:
        # Ask for user input, allow the word 'hint' as a command
        guess = input("Your guess (or type 'hint'): ").lower()
        attempts += 1  # Count the attempt

        # Hint logic
        if guess == 'hint':
            if not hint_used:
                print(f"💡 Hint: The first letter is '{word[0]}'")  # Give first letter
                hint_used = True
                attempts -= 1  # Don’t count hint request as an attempt
            else:
                print("⚠️ You've already used your hint!")  # Only allow once
            continue  # Go back to the start of the loop

        # Check if the guess is correct
        if guess == word:
            end_time = time.time()  # Stop the timer
            elapsed = end_time - start_time  # Calculate time taken
            print(f"✅ Correct! You got it in {attempts} attempt(s).")
            print(f"⏱️ Time taken: {elapsed:.2f} seconds")

            # Update scoreboard if this is a new best performance
            if best_attempts is None or attempts < best_attempts:
                best_attempts = attempts
                print(f"🏆 New best score: {attempts} attempt(s)!")

            if best_time is None or elapsed < best_time:
                best_time = elapsed
                print(f"⏱️ New fastest time: {elapsed:.2f} seconds!")
            break  # Exit the guessing loop

        else:
            print("❌ Incorrect. Try again.")  # Ask to guess again

# Step 5: Overall game loop to allow replay
def main():
    print("🎮 Welcome to the Word Scramble Game!")

    while True:
        play_game()  # Play one round
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            # If user is done playing, print scoreboard
            print("Thanks for playing!")
            if best_attempts is not None and best_time is not None:
                print(f"\n📊 Final Scoreboard:\n - Best Attempts: {best_attempts}\n - Fastest Time: {best_time:.2f} seconds")
            break  # Exit the main loop

# Step 6: Start the game
main()
