// === Compliment Generator Project! ✨ ===
// In this project, we learn:
// - How to create and use functions
// - How to work with strings (words)
// - How to make our programs friendlier and more interactive!

#include <iostream> // Needed for input and output
using namespace std; // So we don't have to write "std::" all the time

// --- Function Declaration ---
// A function called "compliment" that takes a name and returns a nice message!
string compliment(string name) {
    return "You're awesome, " + name + "!"; // Adds the name into a happy sentence
}

int main() {
    string yourName; // A box (variable) to store the user's name

    // Ask the user for their name
    cout << "What's your name? ";
    cin >> yourName; // Save what they type into "yourName"

    // Call (use) the compliment function and show the message
    cout << compliment(yourName) << endl;

    return 0; // End the program
}