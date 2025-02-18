import random
import time

class Character:
    def __init__(self, name, health, attack):
        # Initialize character attributes
        self.name = name
        self.max_health = health
        self.health = health
        self.base_attack = attack
        self.gold = 0
        self.inventory = []
        self.level = 1
        self.exp = 0

    def is_alive(self):
        # Check if the character is still alive
        return self.health > 0

    def take_damage(self, damage):
        # Reduce health when taking damage, ensure it doesn't go below 0
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        # Heal the character, but don't exceed max health
        self.health = min(self.health + amount, self.max_health)

    def get_attack_damage(self):
        # Calculate a random attack damage within a range
        return random.randint(self.base_attack - 2, self.base_attack + 2)

    def gain_exp(self, amount):
        # Gain experience and level up if enough exp is accumulated
        self.exp += amount
        if self.exp >= self.level * 100:
            self.level_up()

    def level_up(self):
        # Increase character stats upon leveling up
        self.level += 1
        self.max_health += 10
        self.health = self.max_health
        self.base_attack += 2
        self.exp = 0
        print(f"\nCongratulations! You've leveled up to level {self.level}!")
        print(f"Your max health is now {self.max_health} and your base attack is {self.base_attack}.")

    def regenerate_health(self):
        # Regenerate health based on character level
        regen_amount = self.level
        self.heal(regen_amount)
        print(f"You regenerate {regen_amount} health.")

    def get_stats(self):
        # Return a string containing all character stats
        return f"{self.name} - Level: {self.level}, Health: {self.health}/{self.max_health}, Attack: {self.base_attack}, Gold: {self.gold}, EXP: {self.exp}/{self.level * 100}"

class Enemy:
    def __init__(self, name, health, attack, gold_reward, exp_reward):
        # Initialize enemy attributes
        self.name = name
        self.health = health
        self.attack = attack
        self.gold_reward = gold_reward
        self.exp_reward = exp_reward

    def is_alive(self):
        # Check if the enemy is still alive
        return self.health > 0

    def take_damage(self, damage):
        # Reduce health when taking damage, ensure it doesn't go below 0
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def get_attack_damage(self):
        # Calculate a random attack damage within a range
        return random.randint(self.attack - 1, self.attack + 1)

def create_character():
    # Prompt user for character name and create a new Character instance
    name = input("Enter your character's name: ")
    return Character(name, health=100, attack=10)

def create_enemy(player_level):
    # Define possible enemy types
    enemies = [
        {"name": "Goblin", "health": 30, "attack": 5, "gold": 10, "exp": 20},
        {"name": "Orc", "health": 50, "attack": 8, "gold": 20, "exp": 35},
        {"name": "Troll", "health": 80, "attack": 12, "gold": 35, "exp": 60},
        {"name": "Dragon", "health": 150, "attack": 20, "gold": 100, "exp": 150}
    ]
    # Randomly select an enemy type
    enemy_type = random.choice(enemies)
    # Calculate level multiplier based on player's level
    level_multiplier = (player_level + random.randint(0, 2)) / 2
    # Create and return a new Enemy instance with scaled attributes
    return Enemy(
        enemy_type["name"],
        int(enemy_type["health"] * level_multiplier),
        int(enemy_type["attack"] * level_multiplier),
        int(enemy_type["gold"] * level_multiplier),
        int(enemy_type["exp"] * level_multiplier)
    )

def battle(player, enemy):
    print(f"A level {enemy.attack // 5} {enemy.name} appears!")
    
    while player.is_alive() and enemy.is_alive():
        # Display current stats
        print("\n" + player.get_stats())
        print(f"{enemy.name} - Health: {enemy.health}")
        
        # Get player action
        action = input("Do you want to [a]ttack, [d]efend, or [r]un? ").lower()
        
        if action == 'a':
            # Player attacks
            player_damage = player.get_attack_damage()
            enemy.take_damage(player_damage)
            print(f"You deal {player_damage} damage to the {enemy.name}.")
            
            if enemy.is_alive():
                # Enemy counterattacks if still alive
                enemy_damage = enemy.get_attack_damage()
                player.take_damage(enemy_damage)
                print(f"The {enemy.name} attacks you for {enemy_damage} damage.")
            else:
                # Enemy defeated
                print(f"You have defeated the {enemy.name}!")
                player.gold += enemy.gold_reward
                player.gain_exp(enemy.exp_reward)
                print(f"You gain {enemy.gold_reward} gold and {enemy.exp_reward} experience.")
                return True
        elif action == 'd':
            # Player defends, reducing incoming damage
            enemy_damage = max(0, enemy.get_attack_damage() - player.level)
            player.take_damage(enemy_damage)
            print(f"You defend against the {enemy.name}'s attack, reducing the damage to {enemy_damage}.")
        elif action == 'r':
            # Player attempts to run away
            if random.random() < 0.5:
                print("You successfully run away!")
                return False
            else:
                print("You failed to run away.")
                enemy_damage = enemy.get_attack_damage()
                player.take_damage(enemy_damage)
                print(f"The {enemy.name} attacks you for {enemy_damage} damage.")
        else:
            print("Invalid action. You lose your turn.")
        
        time.sleep(1)  # Add a short delay for readability
    
    return False

def explore(player):
    # Define possible exploration events
    events = [
        "You find a healing potion and restore 30 health.",
        f"You discover a small treasure chest with {player.level * 10} gold.",
        "You encounter a wise old man who teaches you a new technique. Your base attack increases by 1.",
        "You fall into a trap and lose 15 health.",
        "You find a mysterious artifact that increases your max health by 10."
    ]
    
    # Randomly select and execute an event
    event = random.choice(events)
    print(event)
    
    if "healing potion" in event:
        player.heal(30)
    elif "treasure chest" in event:
        player.gold += player.level * 10
    elif "new technique" in event:
        player.base_attack += 1
    elif "trap" in event:
        player.take_damage(15)
    elif "artifact" in event:
        player.max_health += 10
        player.heal(10)
        player.inventory.append("Mysterious Artifact")
        print("Added Mysterious Artifact to your inventory.")

    time.sleep(1)  # Add a short delay for readability

def main():
    print("Welcome to the Expanded Text RPG!")
    player = create_character()
    
    while player.is_alive():
        # Main game loop
        print("\n--- Main Menu ---")
        print("1. Explore")
        print("2. Rest")
        print("3. View Character Stats")
        print("4. Quit")
        
        choice = input("What would you like to do? ")
        
        if choice == '1':
            # Explore: 70% chance of battle, 30% chance of random event
            if random.random() < 0.7:
                enemy = create_enemy(player.level)
                victory = battle(player, enemy)
                if not player.is_alive():
                    print("Game Over! You have been defeated.")
                    break
            else:
                explore(player)
            player.regenerate_health()
        elif choice == '2':
            # Rest to recover health
            rest_amount = player.max_health // 2
            player.heal(rest_amount)
            print(f"You rest and recover {rest_amount} health.")
            time.sleep(1)
        elif choice == '3':
            # Display character stats and inventory
            print("\n" + player.get_stats())
            print("Inventory:", ", ".join(player.inventory) if player.inventory else "Empty")
            time.sleep(2)
        elif choice == '4':
            # Quit the game
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()