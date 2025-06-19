#include <iostream>
#include <fstream>      // For file input/output (save/load)
#include <vector>
#include <string>
#include <cstdlib>      // For rand, srand
#include <ctime>        // For time (seed RNG)
#include <unistd.h>     // For sleep()
#include <algorithm>    // For std::find
using namespace std;

// Utility function: prints ASCII art and pauses for dramatic effect
void printArt(const string& art) {
    cout << art << endl;
    sleep(1);
}

// Player data: health, mushrooms collected, inventory, location, and day count
struct Player {
    string name;
    int health = 5;
    int mushrooms = 0;
    vector<string> inventory;
    string location = "Forest"; // starting location
    int day = 1;
};

// Monster data: name, health, attack power
struct Monster {
    string name;
    int health;
    int attackPower;
};

// Map system: list of locations and connections for navigation
struct Map {
    vector<string> locations = {"Forest", "River", "Hills", "Cave"};

    // Defines which locations are reachable from current location
    vector<string> getNeighbors(const string& loc) {
        if (loc == "Forest") return {"River", "Hills"};
        if (loc == "River") return {"Forest", "Cave"};
        if (loc == "Hills") return {"Forest", "Cave"};
        if (loc == "Cave") return {"River", "Hills"};
        return {};
    }

    // Show current location and where player can go next
    void showMap(const string& currentLoc) {
        cout << "\n🗺️ You are at: " << currentLoc << endl;
        vector<string> neighbors = getNeighbors(currentLoc);
        cout << "From here, you can travel to:\n";
        for (int i = 0; i < (int)neighbors.size(); i++) {
            cout << i + 1 << ". " << neighbors[i] << endl;
        }
    }
};

// ASCII art for each location
void printLocationArt(const string& loc) {
    if (loc == "Forest") {
        printArt(R"(
    🌲🌲🌲 Forest of Fungoria 🌲🌲🌲
      🍄    🐿️      🌳
    🌲   🌳      🌲
    )");
    } else if (loc == "River") {
        printArt(R"(
    🌊🌊🌊 Riverbank 🌊🌊🌊
      🐟     🌿
    ~~~~~~~~
    )");
    } else if (loc == "Hills") {
        printArt(R"(
    ⛰️⛰️⛰️ Rocky Hills ⛰️⛰️⛰️
      🪨    🌾     🌄
    )");
    } else if (loc == "Cave") {
        printArt(R"(
    🕸️🕸️🕸️ Dark Cave 🕸️🕸️🕸️
      💀     🕷️
    ))");
    }
}

// Prints the player’s current stats and inventory
void showStats(const Player& p) {
    cout << "\n📊 Player Stats:" << endl;
    cout << "Name: " << p.name << " | Day: " << p.day << endl;
    cout << "Health: " << p.health << " | Mushrooms: " << p.mushrooms << endl;
    cout << "Inventory: ";
    if (p.inventory.empty()) cout << "(empty)";
    else {
        for (const string& item : p.inventory) {
            cout << item << " ";
        }
    }
    cout << endl;
}

// Game intro with ASCII art banner and story setup
void intro() {
    cout << R"(
 __  __           _                      ____                      
|  \/  | ___   __| | ___  _ __ ___      / ___| __ _ _ __ ___   ___ 
| |\/| |/ _ \ / _` |/ _ \| '__/ _ \____| |  _ / _` | '_ ` _ \ / _ \
| |  | | (_) | (_| | (_) | | |  __/____| |_| | (_| | | | | | |  __/
|_|  |_|\___/ \__,_|\___/|_|  \___|     \____|\__,_|_| |_| |_|\___|
    )" << endl;

    cout << "\n🌲 Welcome, brave adventurer, to the Forest of Fungoria!" << endl;
    cout << "Your quest is to survive 7 days, collect mushrooms 🍄, and defeat monsters." << endl;
    cout << "Use your wits, items, and courage to succeed!\n" << endl;
}

// Utility function to pause with a short delay for better user experience
void wait(int seconds = 1) {
    sleep(seconds);
}

// Save player state to file
void saveGame(const Player& p) {
    ofstream saveFile("save.txt");
    if (saveFile) {
        saveFile << p.name << "\n"
                 << p.health << "\n"
                 << p.mushrooms << "\n"
                 << p.location << "\n"
                 << p.day << "\n";

        // Save inventory count and items
        saveFile << p.inventory.size() << "\n";
        for (const string& item : p.inventory) {
            saveFile << item << "\n";
        }
        cout << "\n💾 Game saved successfully.\n";
    } else {
        cout << "❌ Failed to save game.\n";
    }
    saveFile.close();
}

// Load player state from file, returns true if successful
bool loadGame(Player& p) {
    ifstream loadFile("save.txt");
    if (!loadFile) {
        cout << "❌ No saved game found.\n";
        return false;
    }

    getline(loadFile, p.name);
    loadFile >> p.health;
    loadFile >> p.mushrooms;
    loadFile.ignore(); // ignore leftover newline
    getline(loadFile, p.location);
    loadFile >> p.day;
    loadFile.ignore();

    int invSize;
    loadFile >> invSize;
    loadFile.ignore();
    p.inventory.clear();
    for (int i = 0; i < invSize; i++) {
        string item;
        getline(loadFile, item);
        p.inventory.push_back(item);
    }
    loadFile.close();
    cout << "\n📂 Game loaded successfully.\n";
    return true;
}

// Monster battle logic: returns true if player survived, false if dead
bool battle(Player& p) {
    // Create a monster with random stats
    vector<string> monsterNames = {"Goblin", "Wicked Spider", "Forest Troll"};
    string monsterName = monsterNames[rand() % monsterNames.size()];
    int monsterHealth = 3 + rand() % 4;  // 3-6 HP
    int monsterAttack = 1 + rand() % 2;  // 1-2 damage

    Monster monster{monsterName, monsterHealth, monsterAttack};

    cout << "\n⚔️ A wild " << monster.name << " appears! Prepare to battle!\n";
    while (monster.health > 0 && p.health > 0) {
        cout << "\nYour Health: " << p.health << " | " << monster.name << " Health: " << monster.health << endl;
        cout << "Choose an action:\n1. Attack\n2. Use Item\n3. Run Away\n> ";
        int action;
        cin >> action;

        if (action == 1) { 
            // Player attacks monster
            int playerAttack = 1 + rand() % 3; // Damage 1-3
            cout << "You attack the " << monster.name << " for " << playerAttack << " damage!\n";
            monster.health -= playerAttack;
            wait();

            if (monster.health <= 0) {
                cout << "🎉 You defeated the " << monster.name << "!\n";
                return true;
            }

            // Monster counterattacks
            cout << "The " << monster.name << " attacks you for " << monster.attackPower << " damage!\n";
            p.health -= monster.attackPower;
            if (p.health <= 0) {
                cout << "💀 You have been slain by the " << monster.name << "...\n";
                return false;
            }
        } 
        else if (action == 2) {
            // Use inventory item
            if (p.inventory.empty()) {
                cout << "Your inventory is empty!\n";
            } else {
                cout << "Inventory:\n";
                for (int i = 0; i < (int)p.inventory.size(); i++) {
                    cout << i + 1 << ". " << p.inventory[i] << endl;
                }
                cout << "Select item number to use, or 0 to cancel: ";
                int itemChoice;
                cin >> itemChoice;

                if (itemChoice > 0 && itemChoice <= (int)p.inventory.size()) {
                    string item = p.inventory[itemChoice - 1];

                    if (item == "Healing Herb") {
                        p.health += 2;
                        if (p.health > 5) p.health = 5;
                        cout << "You used a Healing Herb and restored 2 health!\n";
                        p.inventory.erase(p.inventory.begin() + itemChoice - 1);
                    } 
                    else if (item == "Escape Rope") {
                        cout << "You used an Escape Rope and fled from battle safely.\n";
                        p.inventory.erase(p.inventory.begin() + itemChoice - 1);
                        return true; // Escaped battle, alive
                    } 
                    else {
                        cout << "That item cannot be used now.\n";
                    }
                } else {
                    cout << "Cancelled item use.\n";
                }
            }
        } 
        else if (action == 3) {
            // Attempt to run away
            if (rand() % 2 == 0) {
                cout << "You successfully ran away!\n";
                return true;
            } else {
                cout << "You failed to run away! The monster attacks!\n";
                p.health -= monster.attackPower;
                if (p.health <= 0) {
                    cout << "💀 You have been slain while trying to flee...\n";
                    return false;
                }
            }
        } 
        else {
            cout << "Invalid action. Try again.\n";
        }
    }

    return p.health > 0;
}

// Random encounter in each location: can find mushrooms, monsters, traps, or items
void randomEncounter(Player& p) {
    int roll = rand() % 7; // 0-6

    switch (roll) {
        case 0:
        case 1:
            cout << "\n🍄 You found a wild mushroom! Added to your stash.\n";
            p.mushrooms++;
            break;
        case 2:
            cout << "\n💀 You stepped on a trap and lost 1 health!\n";
            p.health--;
            break;
        case 3:
            cout << "\n🌼 You discovered a Healing Herb!\n";
            p.inventory.push_back("Healing Herb");
            break;
        case 4:
            cout << "\n🎁 You found an Escape Rope!\n";
            p.inventory.push_back("Escape Rope");
            break;
        case 5:
            // Monster battle event
            if (!battle(p)) {
                // Player died in battle
                return;
            }
            break;
        case 6:
            cout << "\n🌳 Quiet day, nothing happens...\n";
            break;
    }
    wait();
}

// Player travel between locations
void travel(Player& p, Map& map) {
    map.showMap(p.location);
    vector<string> neighbors = map.getNeighbors(p.location);

    int choice;
    cout << "Where do you want to go? Enter number: ";
    cin >> choice;

    if (choice > 0 && choice <= (int)neighbors.size()) {
        p.location = neighbors[choice - 1];
        cout << "\nYou travel to " << p.location << "...\n";
        printLocationArt(p.location);
        wait();
    } else {
        cout << "Invalid choice. Staying in " << p.location << ".\n";
    }
}

// Ending game summary and conditions
void gameEnding(const Player& p) {
    cout << "\n===== GAME OVER =====\n";
    cout << "Days Survived: " << p.day - 1 << " / 7\n";
    cout << "Mushrooms Collected: " << p.mushrooms << "\n";
    cout << "Health Remaining: " << p.health << "\n";

    if (p.health <= 0) {
        cout << "\n💀 You died in the Forest of Fungoria.\n";
    } else if (p.mushrooms >= 10) {
        cout << "\n🏆 You collected enough mushrooms and survived! You win!\n";
    } else {
        cout << "\n😞 You survived but didn't collect enough mushrooms....\n";
    }

    cout << "\nThanks for playing!\n";
}

// Main game loop function
void gameLoop(Player& p, Map& map) {
    while (p.day <= 7 && p.health > 0) {
        showStats(p);

        cout << "\nDay " << p.day << ": What would you like to do?\n";
        cout << "1. Explore current location (" << p.location << ")\n";
        cout << "2. Travel to another location\n";
        cout << "3. Use an inventory item\n";
        cout << "4. Save game\n";
        cout << "5. Quit game\n> ";

        int choice;
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "\nExploring " << p.location << "...\n";
                randomEncounter(p);
                p.day++;
                break;
            case 2:
                travel(p, map);
                break;
            case 3:
                if (p.inventory.empty()) {
                    cout << "Inventory is empty.\n";
                } else {
                    cout << "Inventory:\n";
                    for (int i = 0; i < (int)p.inventory.size(); i++) {
                        cout << i + 1 << ". " << p.inventory[i] << endl;
                    }
                    cout << "Select item number to use, or 0 to cancel: ";
                    int itemChoice;
                    cin >> itemChoice;
                    if (itemChoice > 0 && itemChoice <= (int)p.inventory.size()) {
                        string item = p.inventory[itemChoice - 1];
                        if (item == "Healing Herb") {
                            p.health += 2;
                            if (p.health > 5) p.health = 5;
                            cout << "You used a Healing Herb and restored 2 health.\n";
                            p.inventory.erase(p.inventory.begin() + itemChoice - 1);
                        } else if (item == "Escape Rope") {
                            cout << "Escape Rope can only be used in battle.\n";
                        } else {
                            cout << "Item cannot be used now.\n";
                        }
                    } else {
                        cout << "Cancelled.\n";
                    }
                }
                break;
            case 4:
                saveGame(p);
                break;
            case 5:
                cout << "Quitting game...\n";
                return;
            default:
                cout << "Invalid choice, please try again.\n";
        }

        // Check if player died outside battle
        if (p.health <= 0) {
            cout << "You have died due to your injuries...\n";
            break;
        }
    }
}

// Entry point
int main() {
    srand(time(0)); // Seed RNG

    intro();

    Player player;
    Map map;

    cout << "Enter your adventurer's name: ";
    getline(cin, player.name);

    // Ask if player wants to load a saved game
    cout << "Load saved game? (y/n): ";
    char loadChoice;
    cin >> loadChoice;
    cin.ignore(); // flush newline

    if (loadChoice == 'y' || loadChoice == 'Y') {
        if (!loadGame(player)) {
            cout << "Starting a new game instead.\n";
        }
    }

    printLocationArt(player.location);
    wait();

    gameLoop(player, map);
    gameEnding(player);

    return 0;
}
