import random
from enum import Enum
from abc import ABC, abstractmethod
from typing import List, Dict
import time

class Season(Enum):
    HALLOWEEN = 'Halloween'
    CHRISTMAS = 'Christmas'

class Item:
    def __init__(self, name: str, description: str, value: int):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return f"{self.name}: {self.description}"

class Consumable(Item):
    def __init__(self, name: str, description: str, value: int, effect: Dict[str, int]):
        super().__init__(name, description, value)
        self.effect = effect

    def use(self, character: 'Character'):
        for attribute, change in self.effect.items():
            if hasattr(character, attribute):
                setattr(character, attribute, getattr(character, attribute) + change)
        print(f"You used {self.name}!")

class Character(ABC):
    def __init__(self, name: str, health: int, attack: int):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack

    @abstractmethod
    def special_ability(self):
        pass

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage: int):
        self.health = max(0, self.health - damage)

    def heal(self, amount: int):
        self.health = min(self.max_health, self.health + amount)

class Player(Character):
    def __init__(self, name: str, health: int = 100, attack: int = 10):
        super().__init__(name, health, attack)
        self.gold = 0
        self.candy = 0
        self.inventory: List[Item] = []
        self.experience = 0
        self.level = 1

    def special_ability(self):
        self.attack *= 2
        print(f"{self.name} uses their special ability, doubling their attack power!")

    def gain_experience(self, amount: int):
        self.experience += amount
        if self.experience >= self.level * 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.attack += 5
        print(f"Congratulations! {self.name} has reached level {self.level}!")
        print(f"Max Health increased to {self.max_health}")
        print(f"Attack increased to {self.attack}")

    def get_stats(self):
        return (f"{self.name} - Level: {self.level}, Health: {self.health}/{self.max_health}, "
                f"Attack: {self.attack}, Gold: {self.gold}, Candy: {self.candy}, "
                f"Experience: {self.experience}/{self.level * 100}")

class Enemy(Character):
    def __init__(self, name: str, health: int, attack: int, gold_reward: int, candy_reward: int, exp_reward: int):
        super().__init__(name, health, attack)
        self.gold_reward = gold_reward
        self.candy_reward = candy_reward
        self.exp_reward = exp_reward

    def special_ability(self):
        self.health += 20
        print(f"{self.name} uses their special ability, healing 20 health!")

class SeasonalRPG:
    def __init__(self):
        self.player = self.create_character()
        self.current_season = Season.HALLOWEEN
        self.day = 1
        self.items = self.initialize_items()

    @staticmethod
    def create_character():
        name = input("Enter your character's name: ")
        return Player(name)

    @staticmethod
    def initialize_items():
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
        if self.current_season == Season.HALLOWEEN:
            enemies = [
                {"name": "Vampire", "health": 30, "attack": 5, "gold": 5, "candy": 10, "exp": 20},
                {"name": "Werewolf", "health": 50, "attack": 8, "gold": 10, "candy": 20, "exp": 35},
                {"name": "Zombie", "health": 80, "attack": 12, "gold": 15, "candy": 35, "exp": 50}
            ]
        else:  # Christmas
            enemies = [
                {"name": "Grinch", "health": 40, "attack": 6, "gold": 8, "candy": 15, "exp": 25},
                {"name": "Evil Elf", "health": 60, "attack": 10, "gold": 12, "candy": 25, "exp": 40},
                {"name": "Abominable Snowman", "health": 100, "attack": 15, "gold": 20, "candy": 40, "exp": 60}
            ]
        enemy_type = random.choice(enemies)
        return Enemy(enemy_type["name"], enemy_type["health"], enemy_type["attack"],
                     enemy_type["gold"], enemy_type["candy"], enemy_type["exp"])

    def battle(self, enemy: Enemy):
        print(f"A wild {enemy.name} appears!")
        
        while self.player.is_alive() and enemy.is_alive():
            print("\n" + self.player.get_stats())
            print(f"{enemy.name} - Health: {enemy.health}")
            
            action = input("Do you want to [a]ttack, use [s]pecial ability, use [i]tem, or [r]un? ").lower()
            
            if action == 'a':
                enemy.take_damage(self.player.attack)
                print(f"You hit the {enemy.name} for {self.player.attack} damage!")
            elif action == 's':
                self.player.special_ability()
            elif action == 'i':
                self.use_item()
                continue  # Skip enemy's turn if item is used
            elif action == 'r':
                if random.random() < 0.5:
                    print("You successfully run away!")
                    return False
                else:
                    print("You failed to run away.")
            else:
                print("Invalid action. You lose your turn.")

            if enemy.is_alive():
                if random.random() < 0.2:  # 20% chance for enemy to use special ability
                    enemy.special_ability()
                else:
                    self.player.take_damage(enemy.attack)
                    print(f"The {enemy.name} attacks you for {enemy.attack} damage!")
            else:
                print(f"You have defeated the {enemy.name}!")
                self.player.gold += enemy.gold_reward
                self.player.candy += enemy.candy_reward
                self.player.gain_experience(enemy.exp_reward)
                print(f"You gain {enemy.gold_reward} gold, {enemy.candy_reward} candy, and {enemy.exp_reward} experience!")
                return True
        
        return False

    def explore(self):
        events = [
            f"You find a {self.current_season.value} themed treasure chest!",
            "You discover a hidden passage!",
            "You encounter a friendly spirit who shares some wisdom.",
            "You stumble upon a trap!",
            "You find a mysterious artifact."
        ]
        
        event = random.choice(events)
        print(event)
        
        if "treasure chest" in event:
            gold_found = random.randint(10, 30)
            candy_found = random.randint(5, 15)
            self.player.gold += gold_found
            self.player.candy += candy_found
            print(f"You found {gold_found} gold and {candy_found} candy!")
        elif "hidden passage" in event:
            self.player.gain_experience(random.randint(10, 30))
        elif "friendly spirit" in event:
            self.player.attack += 1
            print("Your attack has increased by 1!")
        elif "trap" in event:
            damage = random.randint(5, 15)
            self.player.take_damage(damage)
            print(f"You took {damage} damage from the trap!")
        elif "artifact" in event:
            self.player.inventory.append(Item("Mysterious Artifact", "An enigmatic item of unknown power", 50))
            print("Added Mysterious Artifact to your inventory.")

    def visit_store(self):
        print(f"\n--- {self.current_season.value} Store ---")
        seasonal_items = self.items[self.current_season]
        for i, item in enumerate(seasonal_items, 1):
            print(f"{i}. {item.name} ({item.value} gold) - {item.description}")
        print(f"{len(seasonal_items) + 1}. Return to Main Menu")
        
        choice = input("What would you like to buy? ")
        try:
            choice = int(choice)
            if choice == len(seasonal_items) + 1:
                return
            item = seasonal_items[choice - 1]
            if self.player.gold >= item.value:
                self.player.gold -= item.value
                self.player.inventory.append(item)
                print(f"You bought {item.name}!")
            else:
                print("Not enough gold!")
        except (ValueError, IndexError):
            print("Invalid choice.")

    def use_item(self):
        if not self.player.inventory:
            print("You don't have any items to use.")
            return

        print("\n--- Your Inventory ---")
        for i, item in enumerate(self.player.inventory, 1):
            print(f"{i}. {item}")
        print(f"{len(self.player.inventory) + 1}. Cancel")

        choice = input("Which item would you like to use? ")
        try:
            choice = int(choice)
            if choice == len(self.player.inventory) + 1:
                return
            item = self.player.inventory.pop(choice - 1)
            if isinstance(item, Consumable):
                item.use(self.player)
            else:
                print(f"You can't use the {item.name} right now.")
                self.player.inventory.append(item)
        except (ValueError, IndexError):
            print("Invalid choice.")

    def change_season(self):
        if self.current_season == Season.HALLOWEEN:
            self.current_season = Season.CHRISTMAS
            print("The leaves fall and snow begins to cover the ground. Christmas season has arrived!")
        else:
            self.current_season = Season.HALLOWEEN
            print("The snow melts and pumpkins appear. Halloween season has returned!")

    def main_loop(self):
        print(f"Welcome to the Seasonal RPG! The current season is {self.current_season.value}.")
        
        while self.player.is_alive():
            print(f"\n--- Day {self.day} ---")
            print("1. Explore")
            print("2. Visit Store")
            print("3. Use Item")
            print("4. View Stats")
            print("5. Quit")
            
            choice = input("What would you like to do? ")
            
            if choice == '1':
                if random.random() < 0.7:
                    enemy = self.create_enemy()
                    self.battle(enemy)
                else:
                    self.explore()
            elif choice == '2':
                self.visit_store()
            elif choice == '3':
                self.use_item()
            elif choice == '4':
                print(self.player.get_stats())
                print("Inventory:", ", ".join(item.name for item in self.player.inventory) if self.player.inventory else "Empty")
            elif choice == '5':
                print("Thank you for playing!")
                break
            else:
                print("Invalid choice. Please try again.")

            self.day += 1
            if self.day % 10 == 0:
                self.change_season()

            time.sleep(1)  # Add a small delay between days for better readability

        if not self.player.is_alive():
            print("Game Over! Your character has been defeated.")

if __name__ == "__main__":
    game = SeasonalRPG()
    game.main_loop()