# Reaction Timer Game - Single Try Version
# Measures how fast you press Enter after "Go!"

import time
import random

# Ask the player to get ready
input("\nGet Ready... Press ENTER to start.")

# Wait for a random time between 2 and 5 seconds
time.sleep(random.uniform(2,5))

# Tell the player to GO!
print("GO!")

# Record the time when "Go!" appears
start = time.time()

# Wait for the player to press ENTER
input("Press ENTER as fast as you can!")

# Measure how much time has passed
reaction_time = time.time() - start

# Show the player's reaction time, rounded to 3 decimal places
print(f"Your reaction time: {reaction_time:.3f} seconds.")