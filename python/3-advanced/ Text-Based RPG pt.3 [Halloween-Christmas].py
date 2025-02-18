# Import necessary libraries
import random  # To generate random numbers for events and enemy creation
from enum import Enum  # For defining fixed season names
from abc import ABC, abstractmethod  # For defining abstract base classes and methods
from typing import List, Dict  # To annotate types of lists and dictionaries
import time  # To manage timing and add delays

# Enum to represent different seasons
class Season(Enum):
    HALLOWEEN = 'Halloween'  # Represents the Halloween season
    CHRISTMAS = 'Christmas'  # Represents the Christmas season

# Base class for all items in the game
class Item:
    def __init__(self, name: str, description: str, value: int):
        self.name = name  # Store the name of the item
        self.description = description  # Store a short description of what the item does
        self.value = value  # Store the item's value (e.g., gold cost)

    def __str__(self):
        # This makes it easy to print an item and see its name and description
        return f"{self.name}: {self.description}"

# Consumable items, like potions or food, can affect a player's stats
class Consumable(Item):
    def __init__(self, name: str, description: str, value: int, effect: Dict[str, int]):
        super().__init__(name, description, value)  # Inherit attributes from Item class
        self.effect = effect  # Dictionary storing how the consumable affects the player

    def use(self, character: 'Character'):
        # When a consumable is used, it modifies the player's attributes
        for attribute, change in self.effect.items():
            if hasattr(character, attribute):  # Ensure the attribute exists
                setattr(character, attribute, getattr(character, attribute) + change)
        print(f"You used {self.name}!")

# Character class serves as a blueprint for both players and enemies
class Character(ABC):
    def __init__(self, name: str, health: int, attack: int):
        self.name = name  # Character's name
        self.health = health  # Current health
        self.max_health = health  # Max health value
        self.attack = attack  # Attack power

    @abstractmethod
    def special_ability(self):
        # Abstract method forces subclasses (Player, Enemy) to define their own abilities
        pass

    def is_alive(self):
        # A character is alive as long as their health is above zero
        return self.health > 0

    def take_damage(self, damage: int):
        # Reduce health but ensure it doesn't go below zero
        self.health = max(0, self.health - damage)

    def heal(self, amount: int):
        # Restore health but don't exceed the max health limit
        self.health = min(self.max_health, self.health + amount)

# Player class extends Character, adding unique player features
class Player(Character):
    def __init__(self, name: str, health: int = 100, attack: int = 10):
        super().__init__(name, health, attack)
        self.gold = 0  # Player starts with no gold
        self.candy = 0  # Special collectible currency
        self.inventory: List[Item] = []  # Player's collection of items
        self.experience = 0  # Tracks player progress
        self.level = 1  # Starting level

    def special_ability(self):
        # The player temporarily doubles their attack power
        self.attack *= 2
        print(f"{self.name} uses their special ability, doubling their attack power!")

    def gain_experience(self, amount: int):
        # Add experience points and check if the player should level up
        self.experience += amount
        if self.experience >= self.level * 100:  # Level-up threshold
            self.level_up()

    def level_up(self):
        # Increase level, stats, and reset health when leveling up
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.attack += 5
        print(f"Congratulations! {self.name} has reached level {self.level}!")

    def get_stats(self):
        # Display the player's stats in an easy-to-read format
        return (f"{self.name} - Level: {self.level}, Health: {self.health}/{self.max_health}, "
                f"Attack: {self.attack}, Gold: {self.gold}, Candy: {self.candy}, "
                f"Experience: {self.experience}/{self.level * 100}")

# Enemy class extends Character, defining opponents for the player
class Enemy(Character):
    def __init__(self, name: str, health: int, attack: int, gold_reward: int, candy_reward: int, exp_reward: int):
        super().__init__(name, health, attack)
        self.gold_reward = gold_reward  # Gold earned from defeating this enemy
        self.candy_reward = candy_reward  # Candy earned from defeating this enemy
        self.exp_reward = exp_reward  # Experience points awarded

    def special_ability(self):
        # Enemies can heal themselves using their special ability
        self.health += 20
        print(f"{self.name} uses their special ability, healing 20 health!")

# The main game class, managing game flow, seasons, and interactions
class SeasonalRPG:
    def __init__(self):
        self.player = self.create_character()  # Create a player at game start
        self.current_season = Season.HALLOWEEN  # Game starts in the Halloween season
        self.day = 1  # Track the number of in-game days
        self.items = self.initialize_items()  # Load seasonal items

    @staticmethod
    def create_character():
        # Get player's chosen name and create a new Player object
        name = input("Enter your character's name: ")
        return Player(name)

    @staticmethod
    def initialize_items():
        # Define unique items for Halloween and Christmas seasons
        return {
            Season.HALLOWEEN: [
                Consumable("Candy Corn", "Restores 20 health", 10, {"health": 20}),
                Consumable("Pumpkin Spice Potion", "Increases attack by 5", 20, {"attack": 5}),
            ],
            Season.CHRISTMAS: [
                Consumable("Gingerbread Cookie", "Restores 30 health", 15, {"health": 30}),
                Consumable("Eggnog", "Increases max health by 10", 25, {"max_health": 10}),
            ]
        }

    def create_enemy(self):
        # Create a random enemy based on the current season
        if self.current_season == Season.HALLOWEEN:
            enemies = [
                {"name": "Vampire", "health": 30, "attack": 5, "gold": 5, "candy": 10, "exp": 20},
                {"name": "Werewolf", "health": 50, "attack": 8, "gold": 10, "candy": 20, "exp": 35},
                {"name": "Zombie", "health": 80, "attack": 12, "gold": 15, "candy": 35, "exp": 50}
            ]
        else:  # Christmas season enemies
            enemies = [
                {"name": "Grinch", "health": 40, "attack": 6, "gold": 8, "candy": 15, "exp": 25},
                {"name": "Evil Elf", "health": 60, "attack": 10, "gold": 12, "candy": 25, "exp": 40},
                {"name": "Abominable Snowman", "health": 100, "attack": 15, "gold": 20, "candy": 40, "exp": 60}
            ]
        enemy_type = random.choice(enemies)  # Select a random enemy
        return Enemy(enemy_type["name"], enemy_type["health"], enemy_type["attack"],
                     enemy_type["gold"], enemy_type["candy"], enemy_type["exp"])


    def battle(self, enemy: Enemy):
        # Announce the enemy encounter
        print(f"A wild {enemy.name} appears!")
        
        # Battle loop continues while both the player and enemy are alive
        while self.player.is_alive() and enemy.is_alive():
            # Display player and enemy stats
            print("\n" + self.player.get_stats())
            print(f"{enemy.name} - Health: {enemy.health}")
            
            # Prompt the player to choose an action
            action = input("Do you want to [a]ttack, use [s]pecial ability, use [i]tem, or [r]un? ").lower()
            
            if action == 'a':  # Regular attack
                enemy.take_damage(self.player.attack)
                print(f"You hit the {enemy.name} for {self.player.attack} damage!")
            elif action == 's':  # Special ability
                self.player.special_ability()
            elif action == 'i':  # Use an item
                self.use_item()
                continue  # Skip enemy's turn if item is used
            elif action == 'r':  # Attempt to run away
                if random.random() < 0.5:  # 50% chance of success
                    print("You successfully run away!")
                    return False  # Escape battle
                else:
                    print("You failed to run away.")  # Running failed, enemy still attacks
            else:  # Invalid input
                print("Invalid action. You lose your turn.")

            # Enemy's turn if it's still alive
            if enemy.is_alive():
                if random.random() < 0.2:  # 20% chance the enemy uses its special ability
                    enemy.special_ability()
                else:  # Regular attack
                    self.player.take_damage(enemy.attack)
                    print(f"The {enemy.name} attacks you for {enemy.attack} damage!")
            else:  # Enemy defeated
                print(f"You have defeated the {enemy.name}!")
                self.player.gold += enemy.gold_reward
                self.player.candy += enemy.candy_reward
                self.player.gain_experience(enemy.exp_reward)
                print(f"You gain {enemy.gold_reward} gold, {enemy.candy_reward} candy, and {enemy.exp_reward} experience!")
                return True  # Battle won

        return False  # Player lost the battle

    def explore(self):
        # Possible random events when exploring
        events = [
            f"You find a {self.current_season.value} themed treasure chest!",
            "You discover a hidden passage!",
            "You encounter a friendly spirit who shares some wisdom.",
            "You stumble upon a trap!",
            "You find a mysterious artifact."
        ]
        
        # Select a random event
        event = random.choice(events)
        print(event)
        
        event = random.choice(events)
        print(event)
        
        # Determine outcome based on the event type
        if "treasure chest" in event:  # Find loot
            gold_found = random.randint(10, 30)
            candy_found = random.randint(5, 15)
            self.player.gold += gold_found
            self.player.candy += candy_found
            print(f"You found {gold_found} gold and {candy_found} candy!")
        elif "hidden passage" in event:  # Gain experience
            self.player.gain_experience(random.randint(10, 30))
        elif "friendly spirit" in event:  # Buff player's attack
            self.player.attack += 1
            print("Your attack has increased by 1!")
        elif "trap" in event:  # Take damage
            damage = random.randint(5, 15)
            self.player.take_damage(damage)
            print(f"You took {damage} damage from the trap!")
        elif "artifact" in event:  # Add a special item to inventory
            self.player.inventory.append(Item("Mysterious Artifact", "An enigmatic item of unknown power", 50))
            print("Added Mysterious Artifact to your inventory.")

    def visit_store(self):
        # Display store menu based on the current season
        print(f"\n--- {self.current_season.value} Store ---")
        seasonal_items = self.items[self.current_season]
        
        # List available items
        for i, item in enumerate(seasonal_items, 1):
            print(f"{i}. {item.name} ({item.value} gold) - {item.description}")
        print(f"{len(seasonal_items) + 1}. Return to Main Menu")
        
        # Prompt player to make a purchase
        choice = input("What would you like to buy? ")
        try:
            choice = int(choice)
            if choice == len(seasonal_items) + 1:
                return  # Exit store

            item = seasonal_items[choice - 1]
            if self.player.gold >= item.value:  # Check if player has enough gold
                self.player.gold -= item.value
                self.player.inventory.append(item)
                print(f"You bought {item.name}!")
            else:
                print("Not enough gold!")  # Insufficient funds
        except (ValueError, IndexError):  # Invalid input handling
            print("Invalid choice.")

    def use_item(self):
        # Check if inventory is empty
        if not self.player.inventory:
            print("You don't have any items to use.")
            return

        # Display inventory items
        print("\n--- Your Inventory ---")
        for i, item in enumerate(self.player.inventory, 1):
            print(f"{i}. {item}")
        print(f"{len(self.player.inventory) + 1}. Cancel")

        # Prompt player to choose an item to use
        choice = input("Which item would you like to use? ")
        try:
            choice = int(choice)
            if choice == len(self.player.inventory) + 1:
                return  # Cancel action

            item = self.player.inventory.pop(choice - 1)  # Remove item from inventory
            if isinstance(item, Consumable):  # Check if item is usable
                item.use(self.player)  # Apply item's effect
            else:  # Non-consumable items cannot be used
                print(f"You can't use the {item.name} right now.")
                self.player.inventory.append(item)  # Put item back
        except (ValueError, IndexError):  # Handle invalid inputs
            print("Invalid choice.")

    def change_season(self):
        # Switch between Halloween and Christmas themes
        if self.current_season == Season.HALLOWEEN:
            self.current_season = Season.CHRISTMAS
            print("The leaves fall and snow begins to cover the ground. Christmas season has arrived!")
        else:
            self.current_season = Season.HALLOWEEN
            print("The snow melts and pumpkins appear. Halloween season has returned!")

    def main_loop(self):
        # Welcome message displaying the current season
        print(f"Welcome to the Seasonal RPG! The current season is {self.current_season.value}.")
        
        # Main game loop runs while the player is alive
        while self.player.is_alive():
            print(f"\n--- Day {self.day} ---")
            print("1. Explore")
            print("2. Visit Store")
            print("3. Use Item")
            print("4. View Stats")
            print("5. Quit")
            
            # Get player's choice
            choice = input("What would you like to do? ")
            
            if choice == '1':  # Exploration or battle
                if random.random() < 0.7:  # 70% chance of encountering an enemy
                    enemy = self.create_enemy()
                    self.battle(enemy)
                else:
                    self.explore()  # 30% chance of a random event
            elif choice == '2':  # Store visit
                self.visit_store()
            elif choice == '3':  # Use an item
                self.use_item()
            elif choice == '4':  # Show player stats and inventory
                print(self.player.get_stats())
                print("Inventory:", ", ".join(item.name for item in self.player.inventory) if self.player.inventory else "Empty")
            elif choice == '5':  # Exit game
                print("Thank you for playing!")
                break
            else:
                print("Invalid choice. Please try again.") # Handle invalid inputs
            
            self.day += 1  # Advance game day
            if self.day % 10 == 0:  # Change season every 10 days
                self.change_season()

            time.sleep(1)  # Add a small delay between days for better readability
        
        # Display game over message if player dies
        if not self.player.is_alive():
            print("Game Over! Your character has been defeated.")

# Start the game if the script is run directly
if __name__ == "__main__":
    game = SeasonalRPG()
    game.main_loop()