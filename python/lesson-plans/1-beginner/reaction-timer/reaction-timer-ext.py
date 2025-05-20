import time  # Lets us work with time
import random  # Lets us pick random numbers

def reaction_timer_game():
    # Ask the user how many times they want to try the game
    attempts = int(input("\nHow many times do you want to try? "))
    
    # Initialize the best reaction time as None so we can compare later
    best_time = None

    # Loop for the number of attempts the user wants
    for i in range(attempts):
        print(f"\nAttempt {i + 1}...")  # Show attempt number (starting at 1)
        input("Get ready... Press Enter to start.")  # Wait for user to start
        
        # Wait a random amount of time (2 to 4 seconds) to avoid cheating
        time.sleep(random.uniform(2, 4))

        print("Go!")  # Tell the user to react
        start = time.time()  # Record the start time

        input("Press Enter!")  # Wait for user to react
        rt = time.time() - start  # Calculate reaction time
        print(f"Reaction time: {rt:.3f} seconds")  # Show reaction time

        # Save the best (fastest) time so far
        if best_time is None or rt < best_time:
            best_time = rt

    # After all attempts, print the best reaction time
    print(f"\n🏁 Best time: {best_time:.3f} seconds")

# Uncomment the line below to play the game!
# reaction_timer_game()
