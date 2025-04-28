# 🧹 First, we import a library that lets us pick random numbers
import random

# 🎲 This function "rolls" a dice by picking a random number between 1 and 6
def roll_dice():
    return random.randint(1, 6)

# ⚔️ This function plays a full 5-round battle!
def full_battle():
    rounds = 5            # 🧮 How many rounds we will play
    player_score = 0       # 🧍‍♂️ Player's starting score
    cpu_score = 0          # 🤖 CPU's starting score

    # 🔁 Play 5 rounds
    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        
        # 🎲 Each player rolls TWO dice
        p1 = roll_dice()
        p2 = roll_dice()
        c1 = roll_dice()
        c2 = roll_dice()

        # ➕ Add the two dice together
        player_total = p1 + p2
        cpu_total = c1 + c2

        # 📢 Show the rolls
        print(f"You rolled: {p1} + {p2} = {player_total}")
        print(f"CPU rolled: {c1} + {c2} = {cpu_total}")

        # 🏆 Who wins the round?
        if player_total > cpu_total:
            print("✅ You win this round!")
            player_score += 1   # 🧍‍♂️ Add a point for the player
        elif cpu_total > player_total:
            print("❌ CPU wins this round!")
            cpu_score += 1      # 🤖 Add a point for the CPU
        else:
            print("⚔️ It's a tie this round!") # No points for tie

    # 🏁 After all rounds, who won the whole game?
    print("\n=== Final Scores ===")
    print(f"You: {player_score} | CPU: {cpu_score}")

    if player_score > cpu_score:
        print("🎉 YOU WIN THE BATTLE!")
    elif cpu_score > player_score:
        print("🤖 CPU WINS THE BATTLE!")
    else:
        print("⚔️ IT'S A FINAL TIE!")

# 🧍‍♂️ vs 🤖 Quick single roll game
player_roll = roll_dice()
cpu_roll = roll_dice()

print("\n🎲 You rolled:", player_roll)
print("🤖 CPU rolled:", cpu_roll)

if player_roll > cpu_roll:
    print("✅ You win!")
elif cpu_roll > player_roll:
    print("❌ CPU wins!")
else:
    print("⚔️ It's a tie!")

# 🎮 Now let's play the full battle too!
full_battle()
