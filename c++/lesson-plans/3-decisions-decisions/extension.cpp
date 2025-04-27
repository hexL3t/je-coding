#include <iostream>
#include <cstdlib> // For random number functions
#include <ctime>   // For time() function

using namespace std;

int main(){
    // Set up the random number generator
    srand(static_cast<unsigned int>(time(0)));

    // Pick a random number between 1 and 100
    int secretNumber = rand() % 100 + 1;
    int guess = 0; // Box for the player's guess
    int tries = 0; // Box to count how many guesses the player makes

    // Welcome message
    cout << "======= G U E S S = T H E = N U M B E R =======" << endl;
    cout << "I have chosen a number between 1 and 100." << endl;
    cout << "Try to guess it as fast as you can!" << endl;

    // Game loop - keeps asking until the correct guess
    while (guess != secretNumber){
        cout << "Enter your guess: ";
        cin >> guess; // Get the guess
        tries++; // Add 1 to the number of tries

        if (guess > secretNumber){
            cout << "Too High! Try Again." << endl;
        }
        else if (guess < secretNumber){
            cout << "Too Low! Try Again." << endl;
        }
        else if (guess == secretNumber){
            cout << "🎉 Congratulations! You guessed my number!" << endl;
            cout << "It took you " << tries << " tries." << endl;
            break; // End the loop when guessed correctly
        }
        else {
            cout << "Error: Invalid Number. Try Again." << endl;
        }
    }

    return 0; // End the program
}
