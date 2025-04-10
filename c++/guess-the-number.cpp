/* 
=== Number Guessing Game ===
Let us dive into new concepts like random number generation 
and more complex conditional logic. 

You’ll also see that this project steps up from the basic 
calculator we just built by introducing control flow with loops, 
alongside more user interaction to build on your previous skills. 

So, what’s going on with this C++ project? Let’s break the code down:
    - #include <cstdlib> and #include <ctime>: We need these for using the rand(), 
        srand(), and time() functions.
    - srand(static_cast<unsigned int>(time(0)));: Initializes a random number generator 
        with the current time as the seed value.
    - int secretNumber = rand() % 100 + 1;: Generates a random number between 1 and 100.
    - while loop: This keeps running until the user guesses the correct number.
    - Loop body: The program takes the user's guess and compares it with the secret number, 
        providing hints of whether they are too low or too high.

So when you run this C++ program, it will ask you to guess a number to see whether it matches 
the randomly generated value. 
*/

#include <iostream>
#include <cstdlib>  // For random() functions
#include <ctime>    // for time() functions

using namespace std;

int main(){
    // initialising the random seed
    srand(static_cast<unsigned int>(time(0)));

    // Generate a random number between two values
    int secretNumber = rand() % 100 + 1; // number between 0 & 100
    int guess = 0;

    cout <<  "======= G U E S S = T H E = N U M B E R =======" << endl;
    cout << "I have chosen a number between 1 and 100" << endl;
    cout << "Can you guess what it is?" << endl;

    while (guess != secretNumber){
        cout << "Enter your guess: ";
        cin >> guess;

        if (guess > secretNumber){
            cout << "Too High! Try Again." << endl;
        }
        else if (guess < secretNumber) {
            cout << "Too Low! Try Again." << endl;
        }
        else if (guess == secretNumber){
            cout << "Congratulations! You guessed my number!" << endl;
            break;
        }
        else {
            cout << "Error: Invalid Number. Try Again." << endl;
        }
    }

    return 0;
}