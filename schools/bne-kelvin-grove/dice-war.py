# 🧹 First, we import a special toolbox (called a "library") that helps us do random stuff
import random

# This function is like a dice roller machine
# It randomly picks a number between 1 and 6 -- just like a real dice!
def roll_dice():
    return random.randint(1, 6) # randint() means "random integer" between two numbers (int = whole number)

# This function plays one quick round of the dice game
def quick_match():
    # The player takes  their turn and rolls the dice
    player_roll = roll_dice()

    # The computer (CPU) also rolls for its turn
    cpu_roll = roll_dice()

    # Let's tell the player what both rolls were
    print("\n🎲 You rolled:", player_roll)
    print("🤖 CPU rolled: ", cpu_roll)

    # Time to figure out who won this round!
    if player_roll > cpu_roll:
        print("✅ You Win!") # If your number is bigger, you win!
    elif cpu_roll > player_roll:
        print("❌ CPU Wins!") # If the CPU's number is bigger, it wins!
    else:
        print("⚔️ Its a tie!") # If both numbers are the same, it's a tie - no winner

# ⚔️ This function plays a full 5-round battle between the player and the CPU
def full_battle():
    rounds = 5             # 🧮 How many rounds we will play
    player_score = 0       # 🧍‍♂️ Player's starting score
    cpu_score = 0          # 🤖 CPU's starting score

    # 🔁 Play the game for 5 rounds using a loop
    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")

        # 🎲 Each side rolls TWO dice (for more excitement!)
        p1 = roll_dice()   # First roll for player
        p2 = roll_dice()   # Second roll for player
        c1 = roll_dice()   # First roll for CPU
        c2 = roll_dice()   # Second roll for CPU

        # ➕ Add both dice to get the total for each side
        player_total = p1 + p2
        cpu_total = c1 + c2

        # 📢 Show the results of the dice rolls
        print(f"You rolled: {p1} + {p2} = {player_total}")
        print(f"CPU rolled: {c1} + {c2} = {cpu_total}")

        # 🏆 Decide who wins this round and update scores
        if player_total > cpu_total:
            print("✅ You win this round!")
            player_score += 1  # ✨ Give the player a point
        elif cpu_total > player_total:
            print("❌ CPU wins this round!")
            cpu_score += 1     # ✨ Give the CPU a point
        else:
            print("⚔️ It's a tie this round!")  # No points for either side

    #🏁 After all 5 rounds, show the final scores
    print("\n=== 🧮 Final Scores ===")
    print(f"You: {player_score} | CPU: {cpu_score}")

    # Announce the overall winner of the 5-round battle
    if player_score > cpu_score:
        print("🎉 YOU WIN THE BATTLE!") # Player wins more rounds
    elif cpu_score > player_score:
        print("🤖 CPU WINS THE BATTLE") # CPU Wins more rounds
    else:
        print("⚔️ ITS A FINAL TIE") # Same number of wins

# Let's play one round of the game!
# quick_match()

# Now let's play the full 5-round battle@
full_battle()