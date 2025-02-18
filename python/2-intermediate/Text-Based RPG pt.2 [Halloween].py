import random

# Define the Character class representing the player
class Character:
    def __init__(self, name, health, attack):
        self.name = name  # Player's name
        self.health = health  # Current health of the player
        self.max_health = health  # Maximum health of the player
        self.attack = attack  # Attack power of the player
        self.gold = 0  # Amount of gold the player has
        self.candy = 0  # Amount of candy the player has
        self.inventory = []  # List of items in the player's inventory

    # Method to check if the character is still alive
    def is_alive(self):
        return self.health > 0

    # Method to decrease health when taking damage
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)  # Ensure health doesn't drop below 0

    # Method to heal the character, up to max health
    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)  # Cap healing at max health

    # Method to get the character's current stats as a formatted string
    def get_stats(self):
        return f"{self.name} - Health: {self.health}/{self.max_health}, Attack: {self.attack}, Gold: {self.gold}, Candy: {self.candy}"

# Define the Monster class
class Monster:
    def __init__(self, name, health, attack, gold_reward, candy_reward):
        self.name = name  # Monster's name
        self.health = health  # Monster's health
        self.attack = attack  # Monster's attack power
        self.gold_reward = gold_reward  # Amount of gold the player gets for defeating this monster
        self.candy_reward = candy_reward  # Amount of candy the player gets for defeating this monster

    # Method to check if the monster is alive
    def is_alive(self):
        return self.health > 0

    # Method to decrease the monster's health when it takes damage
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)  # Ensure health doesn't drop below 0

# Function to create a character (player)
def create_character():
    name = input("Enter your trick-or-treater's name: ")  # Prompt for player's name
    return Character(name, health=100, attack=10)  # Create player with initial health and attack

# Function to create a monster
def create_monster():
    monsters = [
        {"name": "Vampire", "health": 30, "attack": 5, "gold": 5, "candy": 10},
        {"name": "Werewolf", "health": 50, "attack": 8, "gold": 10, "candy": 20},
        {"name": "Zombie", "health": 80, "attack": 12, "gold": 15, "candy": 35}
    ]
    monster_type = random.choice(monsters)  # Randomly select a monster from the list
    return Monster(monster_type["name"], monster_type["health"], monster_type["attack"], 
                   monster_type["gold"], monster_type["candy"])

# Function to handle the battle between player and monster
def battle(player, monster):
    print(f"A spooky {monster.name} appears!")  # Announce the appearance of the monster
    
    # Battle loop continues as long as both player and monster are alive
    while player.is_alive() and monster.is_alive():
        print("\n" + player.get_stats())  # Show player stats
        print(f"{monster.name} - Health: {monster.health}")  # Show monster stats
        
        # Ask player for their action: Attack, Run, or Use Item
        action = input("Do you want to [a]ttack, [r]un, or use [i]tem? ").lower()
        
        if action == 'a':  # Player chooses to attack
            monster.take_damage(player.attack)  # Apply damage to the monster
            print(f"You hit the {monster.name} with your plastic pumpkin for {player.attack} damage!")
            
            if monster.is_alive():  # If monster is still alive
                player.take_damage(monster.attack)  # Monster retaliates
                print(f"The {monster.name} scares you for {monster.attack} damage!")
            else:  # If the monster is defeated
                print(f"You have defeated the {monster.name}!")
                player.gold += monster.gold_reward  # Add gold reward
                player.candy += monster.candy_reward  # Add candy reward
                print(f"You gain {monster.gold_reward} gold and {monster.candy_reward} pieces of candy.")
                return True  # Victory
        elif action == 'r':  # Player chooses to run
            if random.random() < 0.5:  # 50% chance to successfully run
                print("You successfully run away, dropping some candy in panic!")
                candy_lost = min(player.candy, 5)  # Lose some candy on running
                player.candy -= candy_lost
                print(f"You lost {candy_lost} pieces of candy.")
                return False  # Player ran away
            else:  # Failed run attempt
                print("You trip over your costume while trying to run away.")
                player.take_damage(monster.attack)  # Player takes damage while running
                print(f"The {monster.name} scares you for {monster.attack} damage!")
        elif action == 'i':  # Player chooses to use an item
            use_item(player)
        else:
            print("Invalid action. You lose your turn.")  # Invalid action

    return False  # If the player or monster is not alive, the battle ends

# Function to handle the exploration event
def explore(player):
    events = [
        "You find a cauldron of healing potion and restore 20 health.",
        "You discover a haunted house with 5 gold and 10 pieces of candy.",
        "You meet a friendly witch who teaches you a new trick. Your attack increases by 2.",
        "You fall into a spiderweb trap and lose 10 health.",
        "You find a mysterious cursed amulet.",
        "You help a ghost and receive 10 gold as a reward.",
        "You find a pumpkin patch with 15 pieces of premium candy."
    ]
    
    event = random.choice(events)  # Randomly select an exploration event
    print(event)
    
    if "healing potion" in event:  # Healing event
        player.heal(20)
    elif "haunted house" in event:  # Gold and candy event
        player.gold += 5
        player.candy += 10
    elif "new trick" in event:  # Attack boost event
        player.attack += 2
    elif "trap" in event:  # Health loss event
        player.take_damage(10)
    elif "cursed amulet" in event:  # Cursed item event
        player.inventory.append("Cursed Amulet")
        print("Added Cursed Amulet to your inventory.")
    elif "ghost" in event:  # Gold reward event
        player.gold += 10
    elif "pumpkin patch" in event:  # Candy reward event
        player.candy += 15

# Function to handle the Halloween store visit
def visit_store(player):
    print("\n--- Halloween Store ---")
    print("1. Health Potion (20 gold)")
    print("2. Attack Boost (30 gold)")
    print("3. Candy to Gold Exchange (10 candy for 5 gold)")
    print("4. Return to Main Menu")
    
    choice = input("What would you like to buy? ")
    
    if choice == '1' and player.gold >= 20:  # Buying health potion
        player.gold -= 20
        player.inventory.append("Health Potion")
        print("You bought a Health Potion!")
    elif choice == '2' and player.gold >= 30:  # Buying attack boost
        player.gold -= 30
        player.attack += 5
        print("You bought an Attack Boost and increased your attack by 5!")
    elif choice == '3' and player.candy >= 10:  # Exchanging candy for gold
        player.candy -= 10
        player.gold += 5
        print("You exchanged 10 candy for 5 gold!")
    elif choice == '4':  # Returning to the main menu
        return
    else:
        print("Invalid choice or not enough resources.")  # Invalid or insufficient resources

# Function to handle using an item from the player's inventory
def use_item(player):
    if not player.inventory:  # Check if the player has any items
        print("You don't have any items to use.")
        return

    print("\n--- Your Inventory ---")
    for i, item in enumerate(player.inventory, 1):  # Display all items in the inventory
        print(f"{i}. {item}")
    print(f"{len(player.inventory) + 1}. Cancel")

    choice = input("Which item would you like to use? ")
    try:
        choice = int(choice)
        if choice == len(player.inventory) + 1:  # If the player chooses to cancel
            return
        item = player.inventory.pop(choice - 1)  # Remove item from inventory
        if item == "Health Potion":
            player.heal(50)  # Use health potion
            print("You used a Health Potion and restored 50 health!")
        elif item == "Cursed Amulet":
            print("The Cursed Amulet glows ominously... Nothing happens.")
            player.inventory.append(item)  # Put the item back in the inventory
        else:
            print(f"You can't use the {item} right now.")
            player.inventory.append(item)  # Put the item back in the inventory
    except (ValueError, IndexError):  # Handle invalid input
        print("Invalid choice.")

# Main game loop
def main():
    print("Welcome to the Spooky Halloween RPG!")
    player = create_character()  # Create the player's character
    
    while player.is_alive():  # Continue the game loop as long as the player is alive
        print("\n--- Main Menu ---")
        print("1. Trick-or-Treat")
        print("2. View Trick-or-Treater Stats")
        print("3. Visit the Halloween Store")
        print("4. Use Item")
        print("5. Quit")
        
        choice = input("What would you like to do? ")
        
        if choice == '1':  # Trick-or-Treat action
            if random.random() < 0.6:  # 60% chance to battle a monster
                monster = create_monster()  # Create a random monster
                victory = battle(player, monster)  # Start a battle
                if not player.is_alive():  # If the player dies during the battle
                    print("Game Over! You've been scared to death.")
                    break
            else:  # If no monster, the player explores
                explore(player)
        elif choice == '2':  # View player stats
            print("\n" + player.get_stats())
            print("Inventory:", ", ".join(player.inventory) if player.inventory else "Empty")
        elif choice == '3':  # Visit the store
            visit_store(player)
        elif choice == '4':  # Use an item from the inventory
            use_item(player)
        elif choice == '5':  # Quit the game
            print("Thank you for playing. Happy Halloween!")
            break
        else:
            print("Invalid choice. Please try again.")  # Invalid menu choice

# Start the game
if __name__ == "__main__":
    main()