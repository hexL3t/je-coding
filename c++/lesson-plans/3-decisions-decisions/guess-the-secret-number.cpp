#include <iostream> // This lets us show messages and get input from the user
using namespace std; // So we don't have to type "std::" every time

int main() { // The starting point of the program
    int guess; // A box (variable) to store the user's guess
    int secret = 7; // The secret number the player needs to guess

    cout << "Guess the secret number (1–10): "; // Ask the player to make a guess
    cin >> guess; // Save the player's guess into the "guess" box

    if (guess == secret) { // Check if the guess is the same as the secret number
        cout << "You got it right!" << endl; // If it's right, congratulate them
    } else { // Otherwise (if the guess is wrong)...
        cout << "Oops! Try again." << endl; // ...tell them to try again
    }

    return 0; // End of the program
}