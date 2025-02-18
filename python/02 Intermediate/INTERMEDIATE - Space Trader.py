def display_inventory(inventory):
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for item, quantity in inventory.items():
            print(f"- {quantity} {item}")

def buy_item(shop, inventory, credits):
    print("Items available:")
    items = list(shop.keys())
    for i, (item, price) in enumerate(shop.items(), 1):
        print(f"{i}. {item} ({price} credits)")
    
    while True:
        choice = input("Enter a number to buy an item, or 'x' to go back: ").lower()
        if choice == 'x':
            return credits
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(items):
                item_to_buy = items[choice_index]
                item_price = shop[item_to_buy]
                if credits < item_price:
                    print(f"Insufficient funds. You need {item_price} credits but only have {credits}.")
                else:
                    credits -= item_price
                    inventory[item_to_buy] = inventory.get(item_to_buy, 0) + 1
                    print(f"Bought {item_to_buy}. Remaining credits: {credits}")
                    return credits
            else:
                print("Invalid choice. Please enter a number from the list or 'b' to go back.")
        except ValueError:
            print("Invalid input. Please enter a number or 'b' to go back.")

def sell_item(inventory, credits):
    if not inventory:
        print("Your inventory is empty.")
        return credits
    
    display_inventory(inventory)
    while True:
        choice = input("What would you like to sell? (or 'x' to go back): ").lower()
        if choice == 'x':
            return credits
        
        matching_item = next((item for item in inventory.keys() if item.lower() == choice), None)
        
        if matching_item:
            sell_price = 5
            inventory[matching_item] -= 1
            if inventory[matching_item] == 0:
                del inventory[matching_item]
            credits += sell_price
            print(f"Sold {matching_item} for {sell_price} credits. New total: {credits}")
            return credits
        else:
            print(f"You don't have that item in your inventory.")
###
def visit_planet(planet_name, inventory, credits, shops):
    print(f"\nWelcome to {planet_name}!")
    shop = shops.get(planet_name)
    if shop:
        print(f"Available at the {planet_name} shop:")
        for i, (item, price) in enumerate(shop.items(), 1):
            print(f"{i}. {item} ({price} credits)")
    
    while True:
        choice = input("What would you like to do? (buy/sell/explore/leave): ").lower()
        if choice == 'buy' and shop:
            credits = buy_item(shop, inventory, credits)
        elif choice == 'sell':
            credits = sell_item(inventory, credits)
        elif choice == 'explore':
            print(f"Exploring {planet_name}... (Imagine exciting discoveries here!)")
        elif choice == 'leave':
            return credits
        else:
            print("Invalid choice. Please choose buy, sell, explore, or leave.")

def travel(planets, current_planet, credits):
    """Handles traveling between planets, with travel cost."""
    travel_cost = 20  # Base travel cost between planets
    if len(planets) > 1:
        print(f"\nTravel options:")
        for i, planet in enumerate(planets, 1):
            if planet != current_planet:
                print(f"{i}. {planet} ({travel_cost} credits)")
        
        while True:
            choice = input("Choose a planet to travel to (or 'x' to go back): ").lower()
            if choice == 'x':
                return current_planet, credits
            
            try:
                destination_index = int(choice) - 1
                if 0 <= destination_index < len(planets) and planets[destination_index] != current_planet:
                    if credits < travel_cost:
                        print(f"Insufficient funds. Travel costs {travel_cost} credits but you only have {credits}.")
                    else:
                        credits -= travel_cost
                        new_planet = planets[destination_index]
                        print(f"Traveling to {new_planet}... Enjoy the ride!")
                        return new_planet, credits
                else:
                    print("Invalid planet. Please choose from the list or enter 'x' to go back.")
            except ValueError:
                print("Invalid input. Please enter a number or 'x' to go back.")
    else:
        print("There are no other planets to travel to.")
        return current_planet, credits

def main():
    """The main game loop."""
    inventory = {}
    credits = 1000
    shops = {
        "Earth": {"Water": 10, "Food": 20},
        "Mars": {"Metals": 50, "Robots": 100},
        "Moon": {"Helium-3": 75},
        "Venus": {"Chemicals": 30, "Rare Gases": 80},
    }
    planets = list(shops.keys())
    current_planet = planets[0]

    print("Welcome to Space Trader!")
    while True:
        print(f"\nYou have {credits} credits.")
        print(f"You are currently on {current_planet}")
        choice = input("What would you like to do? (travel/inventory/visit/quit): ").lower()
        
        if choice == 'travel':
            current_planet, credits = travel(planets, current_planet, credits)
        elif choice == 'inventory':
            display_inventory(inventory)
        elif choice == 'visit':
            credits = visit_planet(current_planet, inventory, credits, shops)
        elif choice == 'quit':
            print("Thanks for playing Space Trader!")
            break
        else:
            print("Invalid choice. Please choose from travel, inventory, visit, or quit.")

if __name__ == "__main__":
    main()