def display_inventory(inventory):
    """
    This function displays the current contents of the player's inventory.
    If the inventory is empty, it will notify the player.
    Otherwise, it will list all items with their quantities.
    """
    if not inventory:
        print("Your inventory is empty.")  # Displayed when inventory is empty
    else:
        print("Your inventory:")
        # Loop through the items in the inventory and display each one with its quantity
        for item, quantity in inventory.items():
            print(f"- {quantity} {item}")

def buy_item(shop, inventory, credits):
    """
    This function allows the player to purchase items from a shop.
    It displays the available items and their prices, and deducts credits from the player's total if they buy an item.
    """
    print("Items available:")
    items = list(shop.keys())  # Convert the dictionary keys to a list for easier indexing
    # Display all items and their prices in the shop
    for i, (item, price) in enumerate(shop.items(), 1):
        print(f"{i}. {item} ({price} credits)")
    
    while True:
        # Prompt the player to enter a choice or exit by typing 'x'
        choice = input("Enter a number to buy an item, or 'x' to go back: ").lower()
        if choice == 'x':
            return credits  # If the player chooses to go back, return the current credits
        try:
            choice_index = int(choice) - 1  # Convert the input to an index
            if 0 <= choice_index < len(items):
                item_to_buy = items[choice_index]  # Get the selected item
                item_price = shop[item_to_buy]  # Get the price of the item
                # Check if the player has enough credits
                if credits < item_price:
                    print(f"Insufficient funds. You need {item_price} credits but only have {credits}.")
                else:
                    # Deduct credits and add the item to the inventory
                    credits -= item_price
                    inventory[item_to_buy] = inventory.get(item_to_buy, 0) + 1
                    print(f"Bought {item_to_buy}. Remaining credits: {credits}")
                    return credits  # Return the updated credits after the purchase
            else:
                print("Invalid choice. Please enter a number from the list or 'b' to go back.")
        except ValueError:
            print("Invalid input. Please enter a number or 'b' to go back.")

def sell_item(inventory, credits):
    """
    This function allows the player to sell items from their inventory.
    It checks if the item exists in the inventory and then updates the inventory and credits accordingly.
    """
    if not inventory:
        print("Your inventory is empty.")  # Notify the player if the inventory is empty
        return credits
    
    display_inventory(inventory)  # Show the inventory to the player
    while True:
        # Prompt the player to input which item they want to sell
        choice = input("What would you like to sell? (or 'x' to go back): ").lower()
        if choice == 'x':
            return credits  # Return credits if the player chooses to go back
        
        # Check if the player has the item they want to sell
        matching_item = next((item for item in inventory.keys() if item.lower() == choice), None)
        
        if matching_item:
            sell_price = 5  # Set a fixed price for selling items
            inventory[matching_item] -= 1  # Decrease the quantity of the item
            if inventory[matching_item] == 0:
                del inventory[matching_item]  # Remove the item if its quantity reaches 0
            credits += sell_price  # Add the selling price to the credits
            print(f"Sold {matching_item} for {sell_price} credits. New total: {credits}")
            return credits  # Return the updated credits after the sale
        else:
            print(f"You don't have that item in your inventory.")  # Notify if the item is not in the inventory

def visit_planet(planet_name, inventory, credits, shops):
    """
    This function allows the player to visit a planet and interact with its shop.
    The player can choose to buy, sell, explore, or leave the planet.
    """
    print(f"\nWelcome to {planet_name}!")
    shop = shops.get(planet_name)  # Get the shop items available on this planet
    if shop:
        print(f"Available at the {planet_name} shop:")
        for i, (item, price) in enumerate(shop.items(), 1):
            print(f"{i}. {item} ({price} credits)")  # Display the available items and their prices
    
    while True:
        # Prompt the player to choose an action
        choice = input("What would you like to do? (buy/sell/explore/leave): ").lower()
        if choice == 'buy' and shop:
            credits = buy_item(shop, inventory, credits)  # Handle buying items
        elif choice == 'sell':
            credits = sell_item(inventory, credits)  # Handle selling items
        elif choice == 'explore':
            print(f"Exploring {planet_name}... (Imagine exciting discoveries here!)")  # Exploration option
        elif choice == 'leave':
            return credits  # Return credits when the player leaves the planet
        else:
            print("Invalid choice. Please choose buy, sell, explore, or leave.")

def travel(planets, current_planet, credits):
    """
    This function allows the player to travel between planets, with a cost in credits for each trip.
    It displays available travel options and deducts the appropriate cost from the player's credits.
    """
    travel_cost = 20  # Define the cost to travel between planets
    if len(planets) > 1:
        print(f"\nTravel options:")
        for i, planet in enumerate(planets, 1):
            if planet != current_planet:
                print(f"{i}. {planet} ({travel_cost} credits)")  # List all planets available to travel to
        
        while True:
            # Prompt the player to choose a planet to travel to
            choice = input("Choose a planet to travel to (or 'x' to go back): ").lower()
            if choice == 'x':
                return current_planet, credits  # Return if the player chooses to go back
            
            try:
                destination_index = int(choice) - 1  # Convert the input to an index
                if 0 <= destination_index < len(planets) and planets[destination_index] != current_planet:
                    if credits < travel_cost:
                        print(f"Insufficient funds. Travel costs {travel_cost} credits but you only have {credits}.")
                    else:
                        credits -= travel_cost  # Deduct travel cost from credits
                        new_planet = planets[destination_index]
                        print(f"Traveling to {new_planet}... Enjoy the ride!")  # Inform the player about the travel
                        return new_planet, credits  # Return the new planet and remaining credits
                else:
                    print("Invalid planet. Please choose from the list or enter 'x' to go back.")
            except ValueError:
                print("Invalid input. Please enter a number or 'x' to go back.")
    else:
        print("There are no other planets to travel to.")  # Notify if no other planets are available
        return current_planet, credits  # Return current planet and credits

def main():
    """The main game loop that handles the flow of the game."""
    inventory = {}  # Initialize an empty inventory
    credits = 1000  # Start with 1000 credits
    shops = {  # Define shops and available items on each planet
        "Earth": {"Water": 10, "Food": 20},
        "Mars": {"Metals": 50, "Robots": 100},
        "Moon": {"Helium-3": 75},
        "Venus": {"Chemicals": 30, "Rare Gases": 80},
    }
    planets = list(shops.keys())  # List of planets
    current_planet = planets[0]  # Start on the first planet

    print("Welcome to Space Trader!")  # Greet the player
    while True:
        print(f"\nYou have {credits} credits.")  # Show the current credits
        print(f"You are currently on {current_planet}")  # Show the current planet
        choice = input("What would you like to do? (travel/inventory/visit/quit): ").lower()
        
        if choice == 'travel':
            current_planet, credits = travel(planets, current_planet, credits)  # Handle travel between planets
        elif choice == 'inventory':
            display_inventory(inventory)  # Show the inventory
        elif choice == 'visit':
            credits = visit_planet(current_planet, inventory, credits, shops)  # Handle visiting the planet's shop
        elif choice == 'quit':
            print("Thanks for playing Space Trader!")  # End the game
            break
        else:
            print("Invalid choice. Please choose from travel, inventory, visit, or quit.")  # Invalid input handling

if __name__ == "__main__":
    main()  # Run the main function to start the game