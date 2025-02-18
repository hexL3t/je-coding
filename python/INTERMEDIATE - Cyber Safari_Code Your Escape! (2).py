# CODE-AN-ADVENTURE
# Cyber Safari: Code Your Escape!
# Story Prompt:
# You're on a school field trip to the prestigious Technos Institute, a cutting-edge research facility
# known for its incredible virtual reality simulations. Today's adventure: a cyber safari through the
# heart of a digital jungle!  But something goes wrong. The simulation malfunctions, trapping you
# inside the program.
# Here's where your coding skills come in! You need to solve puzzles and write Python code to navigate
# the virtual jungle, escape dangers, and find your way back to the real world.

# Intermediate / Advanced
import random
# Add an ASCII art title
print("Welcome to the Technos Institute!")
print("Putting on your VR headset, excitement bubbles as you prepare for your virtual safari...")
print("Suddenly, the world fades. Lush greenery replaces the lab, but a holographic message flickers:")
print('"System Malfunction. Emergency Exit Unavailable." Panic sets in. You\'re trapped!')

print("In front of you, is a vast river with huge lily pads to help cross this river.")
print("A frog the size of you comes up beside you and uses the lily pads to cross,")
print("Except you watch as the frog lands on a slightly damaged lily pad and falls into the water.")
print("There are safe lily pads and unsafe lily pads.")

# Function to determine safe lilypads
def cross_river(num_pads):
    safe_sequence = [] # List to store safe pads
    for i in range(num_pads):
        # Simulate random chance of a safe pad
        is_safe = random.randint(0,1) # 0 is for unsafe, 1 is for safe
        if is_safe:
            safe_sequence.append(i+1)
            print("Hop to pad", i+1)
        else:
            print("Avoid pad", i+1)
    return safe_sequence

# Get the number of lily pads
num_pads = int(input("How many lily pads can you see? > "))

# Call the function and get the safe sequence
safe_pads = cross_river(num_pads)

# Srory continues based on outcome
if len(safe_pads)> 0 :
    print("Following the safe sequence, you carefully hop across the river")
else:
    print("Oh no! There seem to be no safe pads. You fall into the water."
          "Thankfully the malfunction resets, and you find yourself back at the riverbank."
          "Try a different path!")
    
print("\nHaving crossed the treacherous river, you continue your exploration of the digital jungle.")
print("Lush foliage surrounds you, the air is thick with the chirps of unseen creatures.")
print("But your peace is shattered by a screech! A troop of mischievous monkeys swings down from the trees,")
print("snatching your backpack containing your supplies!")
print("Those pesky monkeys! You need to get your backpack back!")

# Function to retrive backpack
def retrieve_backpack(num_attempts):
    backpack_recovered = False
    for attempt in range(num_attempts):
        # Simulate a range of chance success
        success = random.randint(0,1) #0 for failure and 1 for success
        if success:
            backpack_recovered = True
            break # Exit loop if successful
        else:
            print("Attempt" , attempt+1, " : The monkeys are too quick! Try again.")
    if backpack_recovered:
        print("Success! You outsmarted the monkeys and retrieved your backpack")
    else:
        print("The monkeys outsmarted you this time. All attempts failed!")
    