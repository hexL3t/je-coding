import random

# Define a Character class for the player
class Character:
    def __init__(self, name, health, attack):
        # Initialize the player's name, health, attack power, gold, and inventory
        self.name = name
        self.health = health
        self.attack = attack
        self.gold = 0
        self.inventory = []

    # Check if the character is alive (health > 0)
    def is_alive(self):
        return self.health > 0

    # Apply damage to the character and prevent negative health
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    # Heal the character by a specified amount
    def heal(self, amount):
        self.health += amount

    # Get a formatted string with character stats
    def get_stats(self):
        return f"{self.name} - Health: {self.health}, Attack: {self.attack}, Gold: {self.gold}"

# Define an Enemy class for the enemies in the game
class Enemy:
    def __init__(self, name, health, attack, gold_reward):
        # Initialize the enemy's name, health, attack power, and gold reward
        self.name = name
        self.health = health
        self.attack = attack
        self.gold_reward = gold_reward

    # Check if the enemy is alive (health > 0)
    def is_alive(self):
        return self.health > 0

    # Apply damage to the enemy and prevent negative health
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

# Function to create a new character
def create_character():
    name = input("Enter your character's name: ")  # Get the player's name
    return Character(name, health=100, attack=10)  # Return a new Character object with default health and attack

# Function to create a random enemy from a list of predefined enemies
def create_enemy():
    # List of possible enemies with different attributes
    enemies = [
        {"name": "Goblin", "health": 30, "attack": 5, "gold": 10},
        {"name": "Orc", "health": 50, "attack": 8, "gold": 20},
        {"name": "Troll", "health": 80, "attack": 12, "gold": 35}
    ]
    # Randomly select an enemy from the list
    enemy_type = random.choice(enemies)
    return Enemy(enemy_type["name"], enemy_type["health"], enemy_type["attack"], enemy_type["gold"])

# Function to handle the battle between the player and the enemy
def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")  # Announce the enemy

    while player.is_alive() and enemy.is_alive():  # Battle continues until one is defeated
        # Display both player and enemy stats
        print("\n" + player.get_stats())
        print(f"{enemy.name} - Health: {enemy.health}")
        
        # Ask the player whether to attack or run
        action = input("Do you want to [a]ttack or [r]un? ").lower()

        if action == 'a':  # Player chooses to attack
            enemy.take_damage(player.attack)  # Apply damage to the enemy
            print(f"You deal {player.attack} damage to the {enemy.name}.")
            
            if enemy.is_alive():  # If enemy is still alive, it retaliates
                player.take_damage(enemy.attack)
                print(f"The {enemy.name} attacks you for {enemy.attack} damage.")
            else:
                print(f"You have defeated the {enemy.name}!")  # If enemy is defeated
                player.gold += enemy.gold_reward  # Player gains gold
                print(f"You gain {enemy.gold_reward} gold.")
                return True  # Return True to indicate victory
        elif action == 'r':  # Player chooses to run
            if random.random() < 0.5:  # 50% chance of successfully running
                print("You successfully run away!")
                return False  # Return False to indicate running away
            else:
                print("You failed to run away.")  # Failed to escape, enemy attacks
                player.take_damage(enemy.attack)
                print(f"The {enemy.name} attacks you for {enemy.attack} damage.")
        else:
            print("Invalid action. You lose your turn.")  # Invalid input, player loses turn
    
    return False  # Return False if the player is defeated

# Function for random exploration events during the game
def explore(player):
    # List of possible exploration events
    events = [
        "You find a healing potion and restore 20 health.",
        "You discover a small treasure chest with 15 gold.",
        "You encounter a wise old man who teaches you a new technique. Your attack increases by 2.",
        "You fall into a trap and lose 10 health.",
        "You find a mysterious artifact."
    ]
    
    event = random.choice(events)  # Randomly choose an event from the list
    print(event)
    
    if "healing potion" in event:  # If healing potion is found
        player.heal(20)
    elif "treasure chest" in event:  # If treasure chest is found
        player.gold += 15
    elif "new technique" in event:  # If new technique is learned
        player.attack += 2
    elif "trap" in event:  # If a trap is encountered
        player.take_damage(10)
    elif "artifact" in event:  # If a mysterious artifact is found
        player.inventory.append("Mysterious Artifact")
        print("Added Mysterious Artifact to your inventory.")

# Main game loop
def main():
    print("Welcome to the Simple Text RPG!")
    player = create_character()  # Create a new player character

    while player.is_alive():  # Game continues as long as the player is alive
        print("\n--- Main Menu ---")
        print("1. Explore")
        print("2. View Character Stats")
        print("3. Quit")
        
        choice = input("What would you like to do? ")

        if choice == '1':  # Player chooses to explore
            if random.random() < 0.6:  # 60% chance to encounter an enemy
                enemy = create_enemy()  # Create a new enemy
                victory = battle(player, enemy)  # Start a battle
                if not player.is_alive():  # Check if the player is defeated
                    print("Game Over! You have been defeated.")
                    break
            else:
                explore(player)  # If no enemy, trigger exploration event
        elif choice == '2':  # Player chooses to view stats
            print("\n" + player.get_stats())
            print("Inventory:", ", ".join(player.inventory) if player.inventory else "Empty")
        elif choice == '3':  # Player chooses to quit
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")  # Invalid choice, ask again

# Run the main game loop when the script is executed
if __name__ == "__main__":
    main()