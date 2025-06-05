#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>  // sleep() for dramatic effect on Unix systems

using namespace std;

// This function plays a "ding" sound (represented with text) and pauses briefly.
// Use this to give feedback when the player makes a valid selection.
void beep() {
    cout << "*ding!* 🍕" << endl;
    sleep(1); // 1-second pause
}

// This function prints out text slowly, character by character, to simulate a game-style dialogue effect.
// Great for building excitement and making the game feel interactive.
void printSlow(string text, int delay = 30) {
    for (char c : text) {
        cout << c << flush;
        usleep(delay * 1000); // convert delay to microseconds
    }
    cout << endl;
}

// This function introduces the game to the player and asks for their name.
// It uses printSlow to add dramatic flair to the intro story.
string startGame() {
    string name;
    printSlow("🎮 Welcome to... PIZZA QUEST 3000!\n");
    printSlow("You're the newest recruit in the Kingdom of Crust.");
    printSlow("Your mission: Build the Ultimate Pizza to save the village!");
    cout << "\nHero, what is your name? ";
    getline(cin, name); // capture player name
    printSlow("Excellent, " + name + ". Your pizza journey begins now.\n");
    return name;
}

// This function allows the player to choose a pizza size.
// It returns the cost based on the selection and updates the sizeName variable.
double selectSize(string& sizeName) {
    int choice;
    printSlow("Choose your Pizza Size:");
    cout << "1. Small 🧒 ($8)\n2. Medium 🧑 ($10)\n3. Large 🧙 ($12)\n> ";
    cin >> choice;

    switch (choice) {
        case 1: sizeName = "Small"; return 8;
        case 2: sizeName = "Medium"; return 10;
        case 3: sizeName = "Large"; return 12;
        default:
            // If input is invalid, default to Medium
            sizeName = "Medium";
            printSlow("⚠️ Invalid choice. Medium selected by default.");
            return 10;
    }
}

// This function allows the player to choose a crust type.
// Returns the cost of the crust and sets the crustName accordingly.
double selectCrust(string& crustName) {
    int choice;
    printSlow("\nChoose your Crust Type:");
    cout << "1. Thin 🪶 ($2)\n2. Thick 🧱 ($3)\n3. Stuffed 🧀 ($4)\n> ";
    cin >> choice;

    switch (choice) {
        case 1: crustName = "Thin Crust"; return 2;
        case 2: crustName = "Thick Crust"; return 3;
        case 3: crustName = "Stuffed Crust"; return 4;
        default:
            crustName = "Thin Crust";
            printSlow("⚠️ Invalid choice. Thin Crust selected by default.");
            return 2;
    }
}

// This function lets the player select their sauce.
// Uses switch-case for choice and returns price while setting the name.
double selectSauce(string& sauceName) {
    int choice;
    printSlow("\nChoose your Sauce:");
    cout << "1. Tomato 🍅 ($1)\n2. BBQ 🔥 ($1.5)\n3. Garlic 🧄 ($2)\n> ";
    cin >> choice;

    switch (choice) {
        case 1: sauceName = "Tomato"; return 1;
        case 2: sauceName = "BBQ"; return 1.5;
        case 3: sauceName = "Garlic"; return 2;
        default:
            sauceName = "Tomato";
            printSlow("⚠️ Invalid choice. Tomato sauce selected.");
            return 1;
    }
}

// This function allows the player to choose up to 3 toppings.
// Toppings are stored in an array, and the cost is calculated based on the number selected.
double selectToppings(string toppings[], int& count) {
    int choice;
    double total = 0;
    count = 0;

    printSlow("\nChoose your toppings (up to 3). $1.5 each.");
    cout << "1. Pepperoni 🐖\n2. Mushrooms 🍄\n3. Onions 🧅\n4. Pineapple 🍍\n5. Cheese 🧀\n";

    // Loop allows up to 3 toppings. Player can enter 0 to stop early.
    while (count < 3) {
        cout << "> Topping " << (count + 1) << " (0 to finish): ";
        cin >> choice;
        if (choice == 0) break;

        switch (choice) {
            case 1: toppings[count++] = "Pepperoni"; break;
            case 2: toppings[count++] = "Mushrooms"; break;
            case 3: toppings[count++] = "Onions"; break;
            case 4: toppings[count++] = "Pineapple"; break;
            case 5: toppings[count++] = "Cheese"; break;
            default:
                printSlow("❌ Not a valid topping.");
                continue; // don't add to total if invalid
        }

        if (choice >= 1 && choice <= 5) {
            total += 1.5;
            beep(); // confirm topping with a sound
        }
    }

    return total;
}

// This function shows the player a summary of their pizza and total cost.
// Useful for reinforcing variables and output formatting.
void showSummary(const string& name, const string& size, const string& crust, const string& sauce, string toppings[], int topCount, double total) {
    printSlow("\n🧾 Your Legendary Pizza Order:");
    cout << "Hero: " << name << endl;
    cout << "Size: " << size << " - Crust: " << crust << " - Sauce: " << sauce << endl;
    cout << "Toppings: ";
    for (int i = 0; i < topCount; i++) {
        cout << toppings[i];
        if (i < topCount - 1) cout << ", ";
    }
    if (topCount == 0) cout << "None"; // show "None" if no toppings were selected
    cout << endl;
    cout << "Total Gold Required: $" << total << "\n";

    // Celebrate the player’s success
    printSlow("\n🌟 The village rejoices! You have crafted the Ultimate Pizza!");
    printSlow("🎉 Game Complete. Thanks for playing, brave chef!");
}

// Main function: This is where the program begins execution.
// We guide the player through each step of the pizza-building process.
int main() {
    string name = startGame(); // Get player name and show intro story

    // Variables to store player selections
    string size, crust, sauce;
    string toppings[3];
    int toppingCount;

    // Calculate the total cost of the pizza
    double total = 0;
    total += selectSize(size);
    total += selectCrust(crust);
    total += selectSauce(sauce);
    total += selectToppings(toppings, toppingCount);

    // Show the final summary of the pizza order
    showSummary(name, size, crust, sauce, toppings, toppingCount, total);

    return 0;
}
