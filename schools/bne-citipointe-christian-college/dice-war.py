#import libaries
import random

# Roll Dice Function
# It randomly picks a number between 1 - 6 - just like a real dice.
def roll_dice():
    return random.randint(1, 6) # randint() = random integer 

# This function plays one quick round of the dice game
def quick_match():
    # The player takes their turn and rolls the dice
    player_roll = roll_dice()

    # The computer (CPU / AI) rolls the dice for it's turn
    cpu_roll = roll_dice()

    # Prints out the results
    print("\n🎲 You rolled:", player_roll)
    print("🤖 CPU rolled:", cpu_roll)

    # Time to figure out who won the round
    if player_roll > cpu_roll:
        print("✅ You Win!")
    elif cpu_roll > player_roll:
        print("🤖 CPU Win!")
    else: 
        print("⚔️ It's a Tie!")

# This function plays a full 5-round battle between player and the CPU
def full_battle():
    # Variables
    rounds = 5          # How many rounds?
    player_score = 0    # Player starting score
    cpu_score = 0       #  CPU starting score

    # Play the game for the amount of rounds
    for round_num in range (1, rounds + 1):
        print(f"\n--- Round {round_num} ---")

        # Each side rolls TWO dice (for more excitement!)
        p1 = roll_dice()        # First roll = player
        p2 = roll_dice()        # Second roll = player
        c1 = roll_dice()        # First roll = cpu
        c2 = roll_dice()        # Second roll = cpu

        # Add both dice to get the total for each side
        player_total = p1 + p2
        cpu_total = c1 + c2

        # Show the results of the dice rolls
        print(f"🎲 You rolled: {p1} + {p2} = {player_total}")
        print(f"🤖 CPU rolled: {c1} + {c2} = {cpu_total}")

        # Decide who wins the round + update scores
        if player_total > cpu_total:
            print("✅ You win this round!")
            player_score += 1  # ✨ Give the player a point
        elif cpu_total > player_total:
            print("❌ CPU wins this round!")
            cpu_score += 1     # ✨ Give the CPU a point
        else:
            print("⚔️ It's a tie this round!")  # No points for either side

    # Show final scores
    print("\n=== 🏆 Final Scores ===")
    print(f"🎲 You: {player_score} | 🤖 CPU: {cpu_score}")

    # Announce overall winner of the dice battle
    if player_score > cpu_score:
        print("🎉 YOU WIN THE BATTLE!") 
    elif cpu_score > player_score:
        print("🤖 CPU WINS THE BATTLE!")
    else:
        print("⚔️ IT'S A FINAL TIE!")

# Play one round of the game!
# quick_match()

# PLay 5-Round Battle!
full_battle()