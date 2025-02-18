import random

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.max_health = health  # New attribute for max health
        self.attack = attack
        self.gold = 0  # New attribute for gold
        self.candy = 0
        self.inventory = []

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)  # Ensure health doesn't go below 0

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)  # Cap healing at max_health

    def get_stats(self):
        return f"{self.name} - Health: {self.health}/{self.max_health}, Attack: {self.attack}, Gold: {self.gold}, Candy: {self.candy}"

class Monster:
    def __init__(self, name, health, attack, gold_reward, candy_reward):
        self.name = name
        self.health = health
        self.attack = attack
        self.gold_reward = gold_reward
        self.candy_reward = candy_reward

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)  # Ensure health doesn't go below 0

def create_character():
    name = input("Enter your trick-or-treater's name: ")
    return Character(name, health=100, attack=10)

def create_monster():
    monsters = [
        {"name": "Vampire", "health": 30, "attack": 5, "gold": 5, "candy": 10},
        {"name": "Werewolf", "health": 50, "attack": 8, "gold": 10, "candy": 20},
        {"name": "Zombie", "health": 80, "attack": 12, "gold": 15, "candy": 35}
    ]
    monster_type = random.choice(monsters)
    return Monster(monster_type["name"], monster_type["health"], monster_type["attack"], 
                   monster_type["gold"], monster_type["candy"])

def battle(player, monster):
    print(f"A spooky {monster.name} appears!")
    
    while player.is_alive() and monster.is_alive():
        print("\n" + player.get_stats())
        print(f"{monster.name} - Health: {monster.health}")
        
        action = input("Do you want to [a]ttack, [r]un, or use [i]tem? ").lower()
        
        if action == 'a':
            monster.take_damage(player.attack)
            print(f"You hit the {monster.name} with your plastic pumpkin for {player.attack} damage!")
            
            if monster.is_alive():
                player.take_damage(monster.attack)
                print(f"The {monster.name} scares you for {monster.attack} damage!")
            else:
                print(f"You have defeated the {monster.name}!")
                player.gold += monster.gold_reward
                player.candy += monster.candy_reward
                print(f"You gain {monster.gold_reward} gold and {monster.candy_reward} pieces of candy.")
                return True
        elif action == 'r':
            if random.random() < 0.5:
                print("You successfully run away, dropping some candy in panic!")
                candy_lost = min(player.candy, 5)
                player.candy -= candy_lost
                print(f"You lost {candy_lost} pieces of candy.")
                return False
            else:
                print("You trip over your costume while trying to run away.")
                player.take_damage(monster.attack)
                print(f"The {monster.name} scares you for {monster.attack} damage!")
        elif action == 'i':
            use_item(player)
        else:
            print("Invalid action. You lose your turn.")
    
    return False

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
    
    event = random.choice(events)
    print(event)
    
    if "healing potion" in event:
        player.heal(20)
    elif "haunted house" in event:
        player.gold += 5
        player.candy += 10
    elif "new trick" in event:
        player.attack += 2
    elif "trap" in event:
        player.take_damage(10)
    elif "cursed amulet" in event:
        player.inventory.append("Cursed Amulet")
        print("Added Cursed Amulet to your inventory.")
    elif "ghost" in event:
        player.gold += 10
    elif "pumpkin patch" in event:
        player.candy += 15

def visit_store(player):
    print("\n--- Halloween Store ---")
    print("1. Health Potion (20 gold)")
    print("2. Attack Boost (30 gold)")
    print("3. Candy to Gold Exchange (10 candy for 5 gold)")
    print("4. Return to Main Menu")
    
    choice = input("What would you like to buy? ")
    
    if choice == '1' and player.gold >= 20:
        player.gold -= 20
        player.inventory.append("Health Potion")
        print("You bought a Health Potion!")
    elif choice == '2' and player.gold >= 30:
        player.gold -= 30
        player.attack += 5
        print("You bought an Attack Boost and increased your attack by 5!")
    elif choice == '3' and player.candy >= 10:
        player.candy -= 10
        player.gold += 5
        print("You exchanged 10 candy for 5 gold!")
    elif choice == '4':
        return
    else:
        print("Invalid choice or not enough resources.")

def use_item(player):
    if not player.inventory:
        print("You don't have any items to use.")
        return

    print("\n--- Your Inventory ---")
    for i, item in enumerate(player.inventory, 1):
        print(f"{i}. {item}")
    print(f"{len(player.inventory) + 1}. Cancel")

    choice = input("Which item would you like to use? ")
    try:
        choice = int(choice)
        if choice == len(player.inventory) + 1:
            return
        item = player.inventory.pop(choice - 1)
        if item == "Health Potion":
            player.heal(50)
            print("You used a Health Potion and restored 50 health!")
        elif item == "Cursed Amulet":
            print("The Cursed Amulet glows ominously... Nothing happens.")
            player.inventory.append(item)  # Put it back in the inventory
        else:
            print(f"You can't use the {item} right now.")
            player.inventory.append(item)  # Put it back in the inventory
    except (ValueError, IndexError):
        print("Invalid choice.")

def main():
    print("Welcome to the Spooky Halloween RPG!")
    player = create_character()
    
    while player.is_alive():
        print("\n--- Main Menu ---")
        print("1. Trick-or-Treat")
        print("2. View Trick-or-Treater Stats")
        print("3. Visit the Halloween Store")
        print("4. Use Item")
        print("5. Quit")
        
        choice = input("What would you like to do? ")
        
        if choice == '1':
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
            visit_store(player)
        elif choice == '4':
            use_item(player)
        elif choice == '5':
            print("Thank you for playing. Happy Halloween!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()