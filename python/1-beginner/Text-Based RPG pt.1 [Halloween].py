import random

# Define a Character class to represent the player
class Character:
    # Initialize the character with name, health, and attack power
    def __init__(self, name, health, attack):
        self.name = name          # Character's name
        self.health = health      # Character's health
        self.attack = attack      # Character's attack power
        self.gold = 0             # Character's gold, initialized to 0
        self.inventory = []       # Character's inventory, initialized as an empty list

    # Check if the character is still alive (health > 0)
    def is_alive(self):
        return self.health > 0

    # Reduce character's health when taking damage
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:         # Prevent health from going below 0
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
        self.name = name          # Monster's name
        self.health = health      # Monster's health
        self.attack = attack      # Monster's attack power
        self.gold_reward = gold_reward  # Gold reward for defeating the monster

    # Check if the monster is still alive (health > 0)
    def is_alive(self):
        return self.health > 0

    # Reduce monster's health when taking damage
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:         # Prevent health from going below 0
            self.health = 0

# Function to create a new character based on user input
def create_character():
    name = input("Enter your trick-or-treater's name: ")  # Ask the user for a name
    return Character(name, health=100, attack=10)        # Return a new Character object with 100 health and 10 attack

# Function to create a random monster from a list of possible monsters
def create_monster():
    monsters = [
        {"name": "Vampire", "health": 30, "attack": 5, "gold": 10},
        {"name": "Werewolf", "health": 50, "attack": 8, "gold": 20},
        {"name": "Zombie", "health": 80, "attack": 12, "gold": 35}
    ]
    monster_type = random.choice(monsters)  # Randomly choose a monster from the list
    return Monster(monster_type["name"], monster_type["health"], monster_type["attack"], monster_type["gold"])

# Function to handle the battle between the player and a monster
def battle(player, monster):
    print(f"A spooky {monster.name} appears!")  # Announce the monster

    # Loop continues while both the player and monster are alive
    while player.is_alive() and monster.is_alive():
        print("\n" + player.get_stats())  # Show player stats
        print(f"{monster.name} - Health: {monster.health}")  # Show monster stats
        
        action = input("Do you want to [a]ttack or [r]un? ").lower()  # Ask the player for an action
        
        if action == 'a':  # Player chooses to attack
            monster.take_damage(player.attack)  # Monster takes damage from player's attack
            print(f"You hit the {monster.name} with your plastic pumpkin for {player.attack} damage!")
            
            if monster.is_alive():  # If monster is still alive, it attacks back
                player.take_damage(monster.attack)
                print(f"The {monster.name} scares you for {monster.attack} damage!")
            else:  # If monster is defeated
                print(f"You have defeated the {monster.name}!")
                player.gold += monster.gold_reward  # Player earns gold
                print(f"You gain {monster.gold_reward} pieces of gold.")
                return True  # Player wins the battle
        elif action == 'r':  # Player chooses to run
            if random.random() < 0.5:  # 50% chance of escaping
                print("You successfully run away, dropping some gold in panic!")
                return False  # Player runs away
            else:  # If running away fails
                print("You trip over your costume while trying to run away.")
                player.take_damage(monster.attack)  # Monster attacks during the failed escape
                print(f"The {monster.name} scares you for {monster.attack} damage!")
        else:  # Invalid input
            print("Invalid action. You lose your turn.")
    
    return False  # If the loop ends, the player lost or ran away

# Function to handle exploration events where the player can find items or face challenges
def explore(player):
    events = [
        "You find a cauldron of healing potion and restore 20 health.",
        "You discover a haunted house with 15 pieces of gold.",
        "You meet a friendly witch who teaches you a new trick. Your attack increases by 2.",
        "You fall into a spiderweb trap and lose 10 health.",
        "You find a mysterious cursed amulet."
    ]
    
    event = random.choice(events)  # Randomly select an event
    print(event)  # Display the event
    
    if "healing potion" in event:  # If healing potion, restore health
        player.heal(20)
    elif "pieces of gold" in event:  # If gold found, add it to the player's inventory
        player.gold += 15
    elif "new trick" in event:  # If new trick, increase attack power
        player.attack += 2
    elif "trap" in event:  # If trap, damage player
        player.take_damage(10)
    elif "cursed amulet" in event:  # If cursed amulet, add to inventory
        player.inventory.append("Cursed Amulet")
        print("Added Cursed Amulet to your inventory.")

# Main game loop
def main():
    print("Welcome to the Spooky Halloween RPG!")  # Game introduction
    player = create_character()  # Create a new character
    
    while player.is_alive():  # Continue the game while the player is alive
        print("\n--- Main Menu ---")  # Display main menu
        print("1. Trick-or-Treat")
        print("2. View Trick-or-Treater Stats")
        print("3. Quit")
        
        choice = input("What would you like to do? ")  # Get player's menu choice
        
        if choice == '1':  # Trick-or-Treat option
            # 60% chance of encountering a monster, 40% chance of exploring
            if random.random() < 0.6:
                monster = create_monster()  # Create a new monster
                victory = battle(player, monster)  # Battle the monster
                if not player.is_alive():  # If the player dies, end the game
                    print("Game Over! You've been scared to death.")
                    break
            else:  # Explore option
                explore(player)  # Trigger exploration
        elif choice == '2':  # View stats option
            print("\n" + player.get_stats())  # Display player stats
            print("Inventory:", ", ".join(player.inventory) if player.inventory else "Empty")  # Show inventory
        elif choice == '3':  # Quit option
            print("Thank you for playing. Happy Halloween!")  # Exit message
            break
        else:  # Invalid input
            print("Invalid choice. Please try again.")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()  # Start the game