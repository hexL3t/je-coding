/* 
=== Number Guessing Game ===

In this project, we learn some cool new skills:
    - How to make random numbers (so the secret number changes every time!)
    - How to use loops to keep the game going until the player wins
    - How to give hints if the guess is too high or too low

Let's dive in!
*/

#include <iostream> // Lets us show messages and get input
#include <cstdlib>  // Lets us create random numbers
#include <ctime>    // Lets us use the current time (to make random numbers more random)

using namespace std;

int main(){
    // Set up (initialize) the random number generator using the current time
    srand(static_cast<unsigned int>(time(0)));

    // Pick a random number between 1 and 100
    int secretNumber = rand() % 100 + 1; // % 100 makes it between 0-99, so +1 makes it 1-100
    int guess = 0; // Make a box (variable) to store the player's guess

    // Print a welcome message
    cout <<  "======= G U E S S = T H E = N U M B E R =======" << endl;
    cout << "I have chosen a number between 1 and 100" << endl;
    cout << "Can you guess what it is?" << endl;

    // Keep asking the player to guess until they get it right
    while (guess != secretNumber){
        cout << "Enter your guess: ";
        cin >> guess; // Get the player's guess

        // Check if the guess is too high
        if (guess > secretNumber){
            cout << "Too High! Try Again." << endl;
        }
        // Check if the guess is too low
        else if (guess < secretNumber) {
            cout << "Too Low! Try Again." << endl;
        }
        // If the guess is correct
        else if (guess == secretNumber){
            cout << "Congratulations! You guessed my number!" << endl;
            break; // Exit the loop because the player guessed right
        }
        // Catch anything weird (just in case)
        else {
            cout << "Error: Invalid Number. Try Again." << endl;
        }
    }

    return 0; // End the program
}
