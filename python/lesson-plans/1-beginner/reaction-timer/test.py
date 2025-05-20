# Reaction Timer - Multi GAME
# Measures how fast you press Enter after "Go!"

import time
import random

# Reaction Timer - Single Try Version
def singleTry():
    input("Get Ready... \nPress [ENTER] to START")    # Ask the player to get ready
    time.sleep(random.uniform(2,5))                 # Waits for a random time between 2 and 5 secondso!
    print("Go!")                                    # Tell the Player to GO
    start_time = time.time()                        # Start the timer, to record time.
    input("Press [ENTER] as fast as you can.")      # Wait for the player to press ENTER
    reaction_time = time.time() - start_time        # Measure how much time as passed, ending time - start time
    # print("Your reaction time: {:.3f} seconds".format(reaction_time))
    print(f"Your reaction time: {reaction_time:.3f} seconds") # Show the player's reaction time, rounded to 3 decimal places

print("====[ R E A C T I O N = T I M E R ]====")
print("[1] Single Try \t [2] Multi-Round \t [3] Advanced")
user_choice = int(input("Select a game: >"))

if user_choice == 1:
    print("\n==== Single-Version ===")
    singleTry()
elif user_choice == 2:
    print("Multi-Round")
elif user_choice == 3:
    print("Advanced")
else:
    print("Error. Incorrect Choice. Try Again.")