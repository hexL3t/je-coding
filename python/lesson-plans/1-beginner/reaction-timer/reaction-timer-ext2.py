import time
import random

def advanced_reaction_timer_game():
    attempts = int(input("🎮 How many rounds do you want to play? "))
    best_time = None
    worst_time = 0
    total_time = 0
    instructions = ["Press Enter!", "Tap now!", "Go go go!", "Hit it!"]

    for i in range(attempts):
        print(f"\n🕹️ Round {i + 1}")
        input("Ready... Press Enter to prepare.")

        wait_time = random.uniform(2, 4)
        print("Get ready...")  # Don't press early!
        time.sleep(wait_time)
        
        prompt = random.choice(instructions)
        print(prompt)
        start = time.time()

        input()
        reaction_time = time.time() - start
        reaction_time = round(reaction_time, 3)
        total_time += reaction_time

        print(f"⏱️ Your time: {reaction_time} seconds")

        if best_time is None or reaction_time < best_time:
            best_time = reaction_time
        if reaction_time > worst_time:
            worst_time = reaction_time

    average_time = round(total_time / attempts, 3)
    print("\n📊 Game Over! Here are your stats:")
    print(f"✅ Fastest time: {best_time} seconds")
    print(f"❌ Slowest time: {worst_time} seconds")
    print(f"📈 Average time: {average_time} seconds")

# Uncomment to play:
# advanced_reaction_timer_game()
