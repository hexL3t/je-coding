# CODE-AN-ADVENTURE
# Cyber Safari: Code Your Escape!
# Story Prompt:
# You're on a school field trip to the prestigious Technos Institute, a cutting-edge research facility
# known for its incredible virtual reality simulations. Today's adventure: a cyber safari through the
# heart of a digital jungle!  But something goes wrong. The simulation malfunctions, trapping you
# inside the program.
# Here's where your coding skills come in! You need to solve puzzles and write Python code to navigate
# the virtual jungle, escape dangers, and find your way back to the real world.
import random
    # Add an ASCII Art title
print("Welcome to the Technos Institute!")
print("Putting on your VR headset, excitement bubbles as you prepare for your virtual safari...")
print("Suddenly, the world fades. Lush greenery replaces the lab, but a holographic message flickers:")
print('"System Malfunction. Emergency Exit Unavailable." Panic sets in. You\'re trapped!')

while True:
    # ---------- First Part of the Story : Raging River with Huge Lily Pads----------
    print("\nIn front of you, is a vast river with huge lily pads to help cross this river.")
    print("A frog the size of you comes up beside you and uses the lily pads to cross,")
    print("Except you watch as the frog lands on a slightly damaged lily pad and falls into the water.")
    print("There are safe lily pads and unsafe lily pads.")
    
    # Get user input in lowercase
    lilypad_choice = input("Do you want to jump to the first lily pad? [y] or [n]").lower()
    
    if lilypad_choice == 'y':
        safe_count = 0 # Initialise safe pad count
        while safe_count < 3: # Looping until 3 safe pads are reached
            safe_pad = random.randint(1,2) # Simulate random safe pad (1 or 2)
            jump = random.randint(1,2) # Simulate your jump
            
            if jump == safe_pad:
                safe_count += 1
                print(f"You land safely on lily pad {safe_count}. Phew! That was close.")
            else:
                print("Oh no! You landed on a damaged pad and fell into the water!")
                print("Unfortunately, the VR simulation glitches and sends you back to the beginning")
                break # Exit the loop on failure
        else: # Successful crossing after 3 safe jumps
            print(f"Congratulations! You landed on {safe_count} and crossed the river")
            
            # ---------- Next Part of the Story : Monkeys Have Stolen Your Backpack ----------
            print("\nHaving crossed the treacherous river, you continue your exploration of the digital jungle.")
            print("Lush foliage surrounds you, the air is thick with the chirps of unseen creatures.")
            print("But your peace is shattered by a screech! A troop of mischievous monkeys swings down from the trees,")
            print("snatching your backpack containing your supplies!")
            print("Those pesky monkeys! You need to get your backpack back!")
            
            # Multiple choice for retrieving backpack
            attempts = 3 # Set number of attempts
            success = False
            
            for try_num in range(attempts):
                print(f"\nAttempt {try_num + 1}:")
                # Nested loops for different retrieval methods (distract, climb, reason)
                
                for method in ["distract", "climb", "reason", "Say Swiper No Swiping to", "slap"]:
                    choice = input(f"Do you want to try to (a) {method} the monkeys? [y] / [n] > ").lower()
                    
                    if choice == 'y':
                        chance = random.randint(0,1) # Random chance for success
                        if chance:
                            success = True
                            print(f"Success! You {method}ed the monkeys and got your backpack back!")
                            break # Exit inner loop if successsful
                        else:
                            print(f"The monkeys were too quick! Try a different method next time.")
                
                if success:
                    break
                
            if not success:
                print("The monkeys outsmarted you this time. All Attempts Failed!")
                
            print("\nHaving crossed the treacherous river and retrieved your backpack,"
                  " you continue your exploration of the digital jungle")
            
            # --------- Next Chapter, The Temple
            print("Lush foliage surrounds you, the air thick with the chirps of unseen creatures.")
            print("Suddenly, the ground beneath your feet crumbles! You slide down a hidden slope")
            print("and land with a soft thud in a clearing. In front of you is a towering temple.")
            
            print("The grand entrance is adorned with intricate carvings, but the massive doors are sealed shut")
            print("To your left, a narrow passage disappears into the darkness...")
            print("To your right, a winding staircase spirals upwards...")
            
            print("What will you do?")
    
            # User chooses left or right
            choice = input("Will you go left, or right? > ").lower()
            
            if choice == "left":
                print("You cautiously enter the dark passage. The air grows thick and stale as you delve deeper.")
                print("After some time, you reach a dead end. A single, ornately carved chest sits in the dust.")
                
                # Simple Puzzle - guess the number.
                found_key = False
                for attempt in range(3):
                    guess = int(input("Enter a number between 1 and 10 to try and unlock the chest: "))
                    if  guess == 5: # modify the answer to challenge yourself
                        found_key = True
                        print("Success! You guessed the correct code and pry open the chest.")
                        break # Exit loop if successful
                    else:
                        print("The lock remains stubbornly shut. Try again!")
                        
                if found_key:
                    print("Inside the chest, nestled in velvet, lies a gleaming gold key")
                else:
                    print("Disapointed, you turn back. The chest held no key to open the temple doors.")
            
            elif choice == "right":
                print("You ascend the winding staircase, each step echoing in the silence.")
                print("Reaching the top, you find a single, weathered keyhole beside the temple door.")
                
            # Check if the user has the key (obtained from the chest in the left path)
            if found_key and choice == "right": # User has key and chose right path
                print("You reach into your backpack and retrieve the key. It fits perfectly in the lock!")
                print("With a satisfying click, the temple doors creak open, revealing a hidden chamber within.")
                print("Congratulations! You've found a way inside the temple. The adventure continues...")
                
                print("You step inside the hidden chamber, a soft light illuminates a large crystal in the center.")
                print("Strange symbols are etched on the pedestal holding the crystal. What will you do?")
                
                choice = input("A. Touch the crystal (be careful) \tB. Examine the symbols (be cautious)").upper()
                
                if choice == "A": # Risky choice - touching the crystal
                    chance = random.randint(0,1) # 50% chance of success
                    if chance:
                        print("As you reach for the crystal, a warm light engulfs you. The symbols on the pedestal glow,"
                              " and the room begins to shimmer. In a flash, you find yourself back in the Technos "
                              "Institute lab, the VR headset deactivated.")
                        print("You've escaped the simulation! You successfully used your coding skills and courage to navigate"
                              "the digital jungle and the temple's secrets. Congratulations!")
                    else:
                        print("As you touch the crystal, a surge of energy explodes outwards. The room shudders, and the symbols"
                              " flare ominously. Uh oh...")
                        print("The malfunction intensifies, and you're thrown back to the riverbank. Try a different path!")
                        
                elif choice == "B": # Cautious choice - Examining the symbols
                    print("You carefully examine the symbols on the pedestal. After some time, you start to recognise patterns.")
                    print("It seems to be a code...")
                    print("You crack the code! The symbols on the pedestal rearrange, revealing a hidden passage behind it.")
                    print("You step through, ready to face what lies ahead...")
                    
            elif found_key and choice == "left": # User has key but chose left path
                print("You reach into your backpack, but there is no place to use the key here. Perhaps it unlocks something"
                      " on the otherside?")
                break
                
            elif not found_key: # User doesn't have the key
                print("The keyhold is empty. You must find a key to unlock this door.")
                print("Perhaps you should explore the dark passage for a way to open the temple doors...")
                break
                
            else:
                print("Thats not a valid choice. Try 'left' or 'right'")
                choice = input("Choose again: ").lower() # Ask for valid input
                
                
    elif choice == 'n':
        print("You decide to wait for another option. The story continues...")
    
    


