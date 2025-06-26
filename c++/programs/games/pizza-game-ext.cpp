#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <unistd.h>  // sleep(), usleep()

using namespace std;

void beep() {
    cout << "*ding!* 🍕" << endl;
    sleep(1);
}

void printSlow(string text, int delay = 30) {
    for (char c : text) {
        cout << c << flush;
        usleep(delay * 1000);
    }
    cout << endl;
}

// New Function: Mini-game to earn gold
int playMiniGame() {
    string ingredients[5] = {"Cheese", "Tomato", "Pepperoni", "Garlic", "Onion"};
    int correctIndex = rand() % 5;

    printSlow("\n🎲 MINI-GAME: Guess the Secret Ingredient!");
    printSlow("The village elder will reward you with gold if you guess right.");

    cout << "Which ingredient am I thinking of?\n";
    for (int i = 0; i < 5; i++) {
        cout << i + 1 << ". " << ingredients[i] << endl;
    }

    cout << "> Enter your guess (1-5): ";
    int guess;
    cin >> guess;

    if (guess - 1 == correctIndex) {
        printSlow("🎯 Amazing! You guessed correctly!");
        printSlow("💰 You earned 10 gold!\n");
        return 10;
    } else {
        printSlow("❌ Oops! That was not the right ingredient.");
        printSlow("💰 You still earn 3 gold for trying.\n");
        return 3;
    }
}

string startGame() {
    string name;
    printSlow("🎮 Welcome to... PIZZA QUEST 3000!\n");
    printSlow("You're the newest recruit in the Kingdom of Crust.");
    printSlow("Your mission: Build the Ultimate Pizza to save the village!");
    cout << "\nHero, what is your name? ";
    cin.ignore();
    getline(cin, name);
    printSlow("Excellent, " + name + ". Your pizza journey begins now.\n");
    return name;
}

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
            sizeName = "Medium";
            printSlow("⚠️ Invalid choice. Medium selected by default.");
            return 10;
    }
}

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

double selectToppings(string toppings[], int& count) {
    int choice;
    double total = 0;
    count = 0;

    printSlow("\nChoose your toppings (up to 3). $1.5 each.");
    cout << "1. Pepperoni 🐖\n2. Mushrooms 🍄\n3. Onions 🧅\n4. Pineapple 🍍\n5. Cheese 🧀\n";

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
                continue;
        }

        if (choice >= 1 && choice <= 5) {
            total += 1.5;
            beep();
        }
    }

    return total;
}

void showSummary(const string& name, const string& size, const string& crust, const string& sauce, string toppings[], int topCount, double total, int gold) {
    printSlow("\n🧾 Your Legendary Pizza Order:");
    cout << "Hero: " << name << endl;
    cout << "Size: " << size << " - Crust: " << crust << " - Sauce: " << sauce << endl;
    cout << "Toppings: ";
    for (int i = 0; i < topCount; i++) {
        cout << toppings[i];
        if (i < topCount - 1) cout << ", ";
    }
    if (topCount == 0) cout << "None";
    cout << endl;

    cout << "Total Pizza Cost: $" << total << endl;
    cout << "Your Available Gold: $" << gold << endl;

    if (gold >= total) {
        printSlow("\n🌟 The village rejoices! You have crafted the Ultimate Pizza!");
        printSlow("🎉 You had enough gold to pay! Well done, hero!");
    } else {
        printSlow("\n💀 Oh no! You don't have enough gold to pay...");
        printSlow("😢 The village will go hungry tonight...");
    }

    printSlow("\n🎮 Game Over. Thanks for playing!");
}

int main() {
    srand(time(0)); // Seed RNG for mini-game
    string name = startGame();

    int gold = 10;
    printSlow("🪙 You start with 10 gold.");

    cout << "\nWould you like to play the mini-game to earn more gold? (y/n): ";
    char play;
    cin >> play;
    if (play == 'y' || play == 'Y') {
        gold += playMiniGame();
    } else {
        printSlow("Skipping the mini-game. Onward to pizza making!");
    }

    string size, crust, sauce;
    string toppings[3];
    int toppingCount;

    double total = 0;
    total += selectSize(size);
    total += selectCrust(crust);
    total += selectSauce(sauce);
    total += selectToppings(toppings, toppingCount);

    showSummary(name, size, crust, sauce, toppings, toppingCount, total, gold);
    return 0;
}
