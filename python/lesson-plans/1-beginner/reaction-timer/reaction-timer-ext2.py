import time  # This lets us pause the program for a little while.
import random  # This lets the computer pick random numbers and choices.

# This is our reaction timer game!
def advanced_reaction_timer_game():
    # Ask the player how many times they want to play.
    attempts = int(input("🎮 How many rounds do you want to play? "))

    best_time = None  # We'll keep track of the fastest reaction time here.
    worst_time = 0  # We'll keep track of the slowest reaction time here.
    total_time = 0  # We'll use this to calculate the average time at the end.

    # These are fun messages to show the player when it's time to press Enter!
    instructions = ["Press Enter!", "Tap now!", "Go go go!", "Hit it!"]

    # Let's play the game the number of times the player chose!
    for i in range(attempts):
        print(f"\n🕹️ Round {i + 1}")  # Show which round we're on.
        input("Ready... Press Enter to prepare.")  # Wait for player to get ready.

        # Wait a random amount of time (between 2 and 4 seconds) before showing the prompt.
        wait_time = random.uniform(2, 4)
        print("Get ready...")  # Get the player ready, but don't press yet!
        time.sleep(wait_time)  # Wait quietly for a surprise start!

        # Show one of the random instructions to tell the player to press Enter.
        prompt = random.choice(instructions)
        print(prompt)
        start = time.time()  # Remember the exact time the prompt was shown.

        input()  # Wait for the player to press Enter.
        reaction_time = time.time() - start  # Calculate how long it took.
        reaction_time = round(reaction_time, 3)  # Round the time to 3 decimal places.
        total_time += reaction_time  # Add to total time for later average.

        print(f"⏱️ Your time: {reaction_time} seconds")  # Show their reaction time.

        # Update best time if this is the fastest so far.
        if best_time is None or reaction_time < best_time:
            best_time = reaction_time

        # Update worst time if this is the slowest so far.
        if reaction_time > worst_time:
            worst_time = reaction_time

    # Calculate the average reaction time.
    average_time = round(total_time / attempts, 3)

    # Show all the final results!
    print("\n📊 Game Over! Here are your stats:")
    print(f"✅ Fastest time: {best_time} seconds")
    print(f"❌ Slowest time: {worst_time} seconds")
    print(f"📈 Average time: {average_time} seconds")

# To play the game, remove the # from the line below:
# advanced_reaction_timer_game()
