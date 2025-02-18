import random

# Define a Character class to represent the player
class Character:
    # Initialize the character with name, health, and attack power
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        self.gold = 0
        self.inventory = []

    # Check if the character is still alive
    def is_alive(self):
        return self.health > 0

    # Reduce character's health when taking damage
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    # Increase character's health when healing
    def heal(self, amount):
        self.health += amount

    # Get a string representation of the character's stats
    def get_stats(self):
        return f"{self.name} - Health: {self.health}, Attack: {self.attack}, gold: {self.gold}"

# Define a Monster class to represent the enemies
class Monster:
    # Initialize the monster with name, health, attack power, and gold reward
    def __init__(self, name, health, attack, gold_reward):
        self.name = name
        self.health = health
        self.attack = attack
        self.gold_reward = gold_reward

    # Check if the monster is still alive
    def is_alive(self):
        return self.health > 0

    # Reduce monster's health when taking damage
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

# Function to create a new character based on user input
def create_character():
    name = input("Enter your trick-or-treater's name: ")
    return Character(name, health=100, attack=10)

# Function to create a random monster
def create_monster():
    monsters = [
        {"name": "Vampire", "health": 30, "attack": 5, "gold": 10},
        {"name": "Werewolf", "health": 50, "attack": 8, "gold": 20},
        {"name": "Zombie", "health": 80, "attack": 12, "gold": 35}
    ]
    monster_type = random.choice(monsters)
    return Monster(monster_type["name"], monster_type["health"], monster_type["attack"], monster_type["gold"])

# Function to handle the battle between the player and a monster
def battle(player, monster):
    print(f"A spooky {monster.name} appears!")
    
    while player.is_alive() and monster.is_alive():
        print("\n" + player.get_stats())
        print(f"{monster.name} - Health: {monster.health}")
        
        action = input("Do you want to [a]ttack or [r]un? ").lower()
        
        if action == 'a':
            # Player attacks the monster
            monster.take_damage(player.attack)
            print(f"You hit the {monster.name} with your plastic pumpkin for {player.attack} damage!")
            
            if monster.is_alive():
                # Monster attacks back if it's still alive
                player.take_damage(monster.attack)
                print(f"The {monster.name} scares you for {monster.attack} damage!")
            else:
                # Player defeats the monster
                print(f"You have defeated the {monster.name}!")
                player.gold += monster.gold_reward
                print(f"You gain {monster.gold_reward} pieces of gold.")
                return True
        elif action == 'r':
            # Player attempts to run away
            if random.random() < 0.5:
                print("You successfully run away, dropping some gold in panic!")
                return False
            else:
                print("You trip over your costume while trying to run away.")
                player.take_damage(monster.attack)
                print(f"The {monster.name} scares you for {monster.attack} damage!")
        else:
            print("Invalid action. You lose your turn.")
    
    return False

# Function to handle exploration events
def explore(player):
    events = [
        "You find a cauldron of healing potion and restore 20 health.",
        "You discover a haunted house with 15 pieces of gold.",
        "You meet a friendly witch who teaches you a new trick. Your attack increases by 2.",
        "You fall into a spiderweb trap and lose 10 health.",
        "You find a mysterious cursed amulet."
    ]
    
    event = random.choice(events)
    print(event)
    
    if "healing potion" in event:
        player.heal(20)
    elif "pieces of gold" in event:
        player.gold += 15
    elif "new trick" in event:
        player.attack += 2
    elif "trap" in event:
        player.take_damage(10)
    elif "cursed amulet" in event:
        player.inventory.append("Cursed Amulet")
        print("Added Cursed Amulet to your inventory.")

# Main game loop
def main():
    print("Welcome to the Spooky Halloween RPG!")
    player = create_character()
    
    while player.is_alive():
        print("\n--- Main Menu ---")
        print("1. Trick-or-Treat")
        print("2. View Trick-or-Treater Stats")
        print("3. Quit")
        
        choice = input("What would you like to do? ")
        
        if choice == '1':
            # 60% chance of encountering a monster, 40% chance of exploring
            if random.random() < 0.6:
                monster = create_monster()
                victory = battle(player, monster)
                if not player.is_alive():
                    print("Game Over! You've been scared to death.")
                    break
            else:
                explore(player)
        elif choice == '2':
            print("\n" + player.get_stats())
            print("Inventory:", ", ".join(player.inventory) if player.inventory else "Empty")
        elif choice == '3':
            print("Thank you for playing. Happy Halloween!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()