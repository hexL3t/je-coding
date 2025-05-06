# 🧹 First, we import a special toolbox (called a "library") that helps us do random stuff
import random

# 🎲 This function is like a dice roller machine
# It randomly picks a number between 1 and 6 — just like rolling a real die!
def roll_dice():
    return random.randint(1, 6)  # 🌀 randint() means "random integer" between two numbers

# ⚡ This function plays one quick round of the dice game
def quick_match():
    # 🧍‍♂️ The player takes their turn and rolls the dice
    player_roll = roll_dice()

    # 🤖 The computer (CPU) also rolls the dice for its turn
    cpu_roll = roll_dice()

    # 🗣️ Let's tell the player what both rolls were
    print("\n🎲 You rolled:", player_roll)
    print("🤖 CPU rolled:", cpu_roll)

    # 🧠 Time to figure out who won the round!
    if player_roll > cpu_roll:
        print("✅ You win!")   # 🏅 If your number is bigger, you win!
    elif cpu_roll > player_roll:
        print("❌ CPU wins!")  # 💻 If the computer’s number is bigger, it wins!
    else:
        print("⚔️ It's a tie!") # 🫱🫲 If both numbers are the same, it's a tie — no winner this time

# 🚀 Let's play one round of the game!
quick_match()
