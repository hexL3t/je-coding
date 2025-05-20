# 🕹️ Reaction Timer Game

Test your reflexes with this fun and beginner-friendly Python project!

This repository includes three versions of a reaction timer game:

1. [Basic Version](#1-basic_reaction_timerpy)
2. [Multi-Round Version](#2-reaction_timer_gamepy)
3. [Advanced Version](#3-advanced_reaction_timer_gamepy)

---

## 📁 Project Files

### 1. `basic_reaction_timer.py`
🔰 **Level: Beginner**

A single-attempt game to measure your reaction speed.

#### Features:
- One reaction test
- Waits a random amount of time (2–5 seconds)
- Measures how quickly the player presses Enter after "Go!"

#### Key Concepts:
- `input()`, `time.sleep()`, `random.uniform()`, `time.time()`

```python
import time
import random

input("\nGet ready... Press Enter to start.")
time.sleep(random.uniform(2, 5))
print("Go!")
start = time.time()
input("Press Enter as fast as you can!")
reaction_time = time.time() - start
print(f"Your reaction time: {reaction_time:.3f} seconds")
```

### 2. `reaction_timer_game.py`

🧪 **Level: Intermediate**

A multi-round version of the game that records the player's best time.
Features:

* Choose how many attempts
* Displays reaction time for each round
* Shows the fastest time at the end

#### Key Concepts:
* for loops
* Conditional logic
* Storing and comparing values

### 3. `advanced_reaction_timer_game.py`

🚀 **Level: Intermediate+**

A more detailed game with stats and randomized prompts.
Features:
* Random instructions each round (e.g., “Go go go!”, “Tap now!”)
* Tracks:
    * Fastest time
    * Slowest time
    * Average reaction time
    * Prevents predictability using random.uniform()

#### Key Concepts:
* random.choice()
* Aggregating stats across multiple rounds
* Better user feedback and cleaner formatting

### 🎯 Learning Goals
This project is great for practicing:
* Real-time interaction with users
* Timing and random delays
* Storing and comparing performance data
* Writing clean loops and conditionals
* Output formatting and user-friendly prompts

### ▶️ How to Run
* Clone or download this repository
* Make sure Python 3 is installed
* In a terminal or command prompt, run:
  * python basic_reaction_timer.py
  * python reaction_timer_game.py
  * python advanced_reaction_timer_game.py

## 🧠 Extension Ideas
* Add a countdown or sound effects
* False start detection (penalty for pressing too early)
* 2-player battle mode
* Save results to a file
* Create a GUI version with tkinter or pygame