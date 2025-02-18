import random

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        self.gold = 0
        self.inventory = []

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount

    def get_stats(self):
        return f"{self.name} - Health: {self.health}, Attack: {self.attack}, Gold: {self.gold}"

class Enemy:
    def __init__(self, name, health, attack, gold_reward):
        self.name = name
        self.health = health
        self.attack = attack
        self.gold_reward = gold_reward

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

def create_character():
    name = input("Enter your character's name: ")
    return Character(name, health=100, attack=10)

def create_enemy():
    enemies = [
        {"name": "Goblin", "health": 30, "attack": 5, "gold": 10},
        {"name": "Orc", "health": 50, "attack": 8, "gold": 20},
        {"name": "Troll", "health": 80, "attack": 12, "gold": 35}
    ]
    enemy_type = random.choice(enemies)
    return Enemy(enemy_type["name"], enemy_type["health"], enemy_type["attack"], enemy_type["gold"])

def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")
    
    while player.is_alive() and enemy.is_alive():
        print("\n" + player.get_stats())
        print(f"{enemy.name} - Health: {enemy.health}")
        
        action = input("Do you want to [a]ttack or [r]un? ").lower()
        
        if action == 'a':
            enemy.take_damage(player.attack)
            print(f"You deal {player.attack} damage to the {enemy.name}.")
            
            if enemy.is_alive():
                player.take_damage(enemy.attack)
                print(f"The {enemy.name} attacks you for {enemy.attack} damage.")
            else:
                print(f"You have defeated the {enemy.name}!")
                player.gold += enemy.gold_reward
                print(f"You gain {enemy.gold_reward} gold.")
                return True
        elif action == 'r':
            if random.random() < 0.5:
                print("You successfully run away!")
                return False
            else:
                print("You failed to run away.")
                player.take_damage(enemy.attack)
                print(f"The {enemy.name} attacks you for {enemy.attack} damage.")
        else:
            print("Invalid action. You lose your turn.")
    
    return False

def explore(player):
    events = [
        "You find a healing potion and restore 20 health.",
        "You discover a small treasure chest with 15 gold.",
        "You encounter a wise old man who teaches you a new technique. Your attack increases by 2.",
        "You fall into a trap and lose 10 health.",
        "You find a mysterious artifact."
    ]
    
    event = random.choice(events)
    print(event)
    
    if "healing potion" in event:
        player.heal(20)
    elif "treasure chest" in event:
        player.gold += 15
    elif "new technique" in event:
        player.attack += 2
    elif "trap" in event:
        player.take_damage(10)
    elif "artifact" in event:
        player.inventory.append("Mysterious Artifact")
        print("Added Mysterious Artifact to your inventory.")

def main():
    print("Welcome to the Simple Text RPG!")
    player = create_character()
    
    while player.is_alive():
        print("\n--- Main Menu ---")
        print("1. Explore")
        print("2. View Character Stats")
        print("3. Quit")
        
        choice = input("What would you like to do? ")
        
        if choice == '1':
            if random.random() < 0.6:
                enemy = create_enemy()
                victory = battle(player, enemy)
                if not player.is_alive():
                    print("Game Over! You have been defeated.")
                    break
            else:
                explore(player)
        elif choice == '2':
            print("\n" + player.get_stats())
            print("Inventory:", ", ".join(player.inventory) if player.inventory else "Empty")
        elif choice == '3':
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()