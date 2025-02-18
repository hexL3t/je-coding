# CODE-AN-ADVENTURE
# Cyber Safari: Code Your Escape!

# Story Prompt:
# You're on a school field trip to the prestigious Technos Institute, a cutting-edge research facility
# known for its incredible virtual reality simulations. Today's adventure: a cyber safari through the
# heart of a digital jungle! But something goes wrong. The simulation malfunctions, trapping you
# inside the program.
# Here's where your coding skills come in! You need to solve puzzles and write Python code to navigate
# the virtual jungle, escape dangers, and find your way back to the real world.

# Intermediate / Advanced
import random


# Add an ASCII art title (you can find some cool ASCII art generators online!)
print("Welcome to the Technos Institute!")
print("Putting on your VR headset, excitement bubbles as you prepare for your virtual safari...")
print("Suddenly, the world fades. Lush greenery replaces the lab, but a holographic message flickers:")
print('"System Malfunction. Emergency Exit Unavailable." Panic sets in. You\'re trapped!')

print("In front of you, is a vast river with huge lily pads to help cross this river.")
print("A frog the size of you comes up beside you and uses the lily pads to cross,")
print("Except you watch as the frog lands on a slightly damaged lily pad and falls into the water.")
print("There are safe lily pads and unsafe lily pads.")


# Function to determine safe lilypads. This function simulates randomly generated safe and unsafe pads
# for the player to hop across the river.
def cross_river(num_pads):
  """
  This function simulates a river crossing using lily pads. Some pads are safe (return True),
  and others are unsafe (return False). The player needs to follow the messages to hop across
  without falling in.

  Args:
      num_pads: The total number of lily pads to cross the river.

  Returns:
      A list containing the indexes of the safe lily pads (starting from 1).
  """
  safe_sequence = []  # List to store the indexes of safe pads
  for i in range(num_pads):
    # Simulate random chance of a safe pad (0 for unsafe, 1 for safe)
    is_safe = random.randint(0, 1)
    if is_safe:
      safe_sequence.append(i + 1)
      print("Hop to pad", i + 1)
    else:
      print("Avoid pad", i + 1)
  return safe_sequence


# Get the number of lily pads from the user
num_pads = int(input("How many lily pads can you see? > "))

# Call the function and get the safe sequence
safe_pads = cross_river(num_pads)

# Story continues based on outcome
if len(safe_pads) > 0:
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


# Function to retrieve backpack. This function simulates a series of attempts to retrieve the backpack
# from the monkeys. There's a random chance of success on each attempt.
def retrieve_backpack(num_attempts):
  """
  This function simulates retrieving your backpack from the monkeys. There's a random chance
  of success on each attempt (0 for failure, 1 for success).

  Args:
      num_attempts: The number of times the player tries to retrieve the backpack.
  """
  backpack_recovered = False
  for attempt in range(num_attempts):
    # Simulate a range of chance success (0 for failure and 1 for success)
    success = random.randint(0, 1)
    if success:
      backpack_recovered = True
      break  # Exit loop if successful
    else:
      print("Attempt", attempt + 1, ": The monkeys are too quick! Try again.")
  if backpack_recovered:
    print("Success! You outsmarted the monkeys and retrieved your backpack")
  else:
    print("The monkeys outsmarted you this time. All attempts failed!")

# Get number of attempts from user
num_attempts = int(input("How many attempts will you try to retrieve your backpack? > "))

# Call retrieve_backpack with user input
retrieve_backpack(num_attempts)

print("\nHaving crossed the trecherous river and recieved your backpack,"
      "you continue your exploration of the digital jungle.")

# Next part of the journey
print("Having felt like you've walked until the end of the earth, you finally break through some lush,"
      "jungle floor fauna. In front of you is a towering temple.")
print("The grand entrance is adorned with intricate carvings, but the massive doors are sealed shut.")
print("To your left, a narrow passage disappears into darkness."
      "To your right, a winding staircase spirals upwards.")
print("You need to find a way inside the temple. What will you do?")


def explore_temple(choice):
  """
  This function explores the temple based on the user's choice (left or right).

  Args:
      choice: The user's choice ("left" or "right").

  Returns:
      True if the user successfully enters the temple, False otherwise.
  """
  if choice.lower() == "left":
    print("You cautiously enter the dark passage. The air grows thick and stale as you delve deeper.")
    print("After some time, you reach a dead end. A single, ornately carved chest sits in the dust.")

    found_key = False
    for attempt in range(3):
      for code in range(1000):  # Adjust for difficulty
        # Simulate random chance of correct attempts
        if random.randint(0, 1):
          found_key = True
          print(f"Attempt: {attempt+1}, Code {code}: Success! You pry open the chest.")
          break  # Break inner loop if successful
        else:
          print(f"Attempt: {attempt+1}, Code {code}: The lock remains stubbornly shut.")
      if found_key:
        break  # Exit outer loop if key is found
    if found_key:
      print("Inside the chest, nestled in velvet, lies a gleaming gold key.")
      return True  # Return if key is found
    else:
      print("Disappointed, you turn back. The chest held no key to open the temple doors.")
      return False  # Return False if key is not found
  elif choice.lower() == "right":
    print("You ascend the winding staircase, each step echoing in the silence.")
    print("Reaching the top, you find a single, weathered keyhole beside the temple door.")
    # Check if the player has the key (obtained from the chest)
    if has_key:
      print("You reach into your backpack and retrieve the key. It fits perfectly in the lock!")
      print("With a satisfying click, the temple doors creak open, revealing a hidden chamber within.")
      return True  # Return True if key opens the door
    else:
      print("The keyhole is empty. You must find a key to unlock this door. Perhaps the dark passage holds the answer?")
      return False  # Return False if no key
  else:
    print("That's not a valid choice. Try 'left' or 'right'.")
    return explore_temple(input("Choose again: "))  # Recursively call function for invalid input

# Flag to track if the key is found from the chest
has_key = True  # Assuming the user retrieved the key from previous part

# Explore the temple based on user choice (already achieved success on right choice)
choice = input("Will you go left (dark passage) or right (winding staircase)? ")
success = explore_temple(choice)  # Since we've set has_key to True simulating a successful retrieval

if success:
    print("Congratulations! You've found a way inside the temple. The adventure continues...")
    print("You step inside the hidden chamber, your eyes adjusting to the dim light.")
    print("In the center of the room, a pedestal holds a glowing orb. Strange symbols line its surface.")
    print("What will you do?")
    choice = input("A. Touch the orb (be careful!) B. Examine the symbols on the pedestal (be cautious)").upper()
    if choice == "A":
      # Risky choice - touching the orb
      chance = random.randint(0, 1)  # 50% chance of success
      if chance:
        print("As you reach for the orb, a warm light engulfs you. The symbols on the pedestal glow, and the room begins to shimmer. In a flash, you find yourself back in the Technos Institute lab, the VR headset deactivated.")
        print("You've escaped the simulation! You successfully used your coding skills and courage to navigate the digital jungle and the temple's secrets. Congratulations!")
      else:
        print("As you touch the orb, a surge of energy explodes outwards. The room shudders, and the symbols flare ominously. Uh oh...")
        # Add a consequence for a failed risky choice (e.g., restart at the river, teleport to a different challenge room)
        print("The malfunction intensifies, and you're thrown back to the riverbank. Try a different path!")
    elif choice == "B":
      # Cautious choice - examining the symbols
      print("You carefully examine the symbols on the pedestal. After some time, you start to recognize patterns. It seems to be a code...")
      # Add a logic puzzle here where the user has to decipher the symbols based on clues from the game
      # If successful, continue with the escape
      print("You crack the code! The pedestal clicks, and a hidden passage opens behind it. You step through, ready to face what lies ahead...")
      # Add a new area or challenge here
    else:
      print("That's not a valid choice. Try 'A' or 'B'.")
      explore_temple(input("What will you do? "))  # Recursively call for invalid input
else:
    print("It seems you haven't found the right path yet. Don't give up, explorer!")
