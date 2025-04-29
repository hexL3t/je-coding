# 🧹 First, we import a library that lets us pick random numbers
import random

# 🎲 This function will "roll" a dice by picking a random number from 1 to 6
def roll_dice():
    return random.randint(1, 6)

# 🧍‍♂️ The player rolls the dice!
player_roll = roll_dice()

# 🤖 The computer (CPU) also rolls the dice!
cpu_roll = roll_dice()

# 📢 Let's show everyone what they rolled!
print("\n🎲 You rolled:", player_roll)
print("🤖 CPU rolled:", cpu_roll)

# 🏆 Now, let's figure out who won!
if player_roll > cpu_roll:
    print("✅ You win!")   # If you rolled higher, you win!
elif cpu_roll > player_roll:
    print("❌ CPU wins!")  # If the computer rolled higher, they win!
else:
    print("⚔️ It's a tie!") # If you both rolled the same number, it's a tie!
