// === Magic 8-Ball Simulator 🎱 ===
// In this project, we learn:
// - How to use random numbers
// - How to work with arrays (lists of things)
// - How to answer user questions in a fun way!

#include <iostream> // For input and output
#include <cstdlib>  // For random numbers
#include <ctime>    // To set a random seed (different results every time)

using namespace std;

int main() {
    // Create a list of possible Magic 8-Ball answers
    string answers[] = {
        "Yes, definitely!",
        "Ask again later...",
        "No way!",
        "It is certain.",
        "Don't count on it.",
        "Signs point to yes!",
        "Very doubtful.",
        "Without a doubt!"
    };

    // Set up the random number generator
    srand(static_cast<unsigned int>(time(0)));

    string question; // A variable to hold the user's question

    cout << "🎱 Welcome to the Magic 8-Ball! 🎱" << endl;
    cout << "Ask any yes-or-no question: ";
    getline(cin, question); // Get the whole line (including spaces)

    // Pick a random answer
    int randomIndex = rand() % 8; // Pick a number between 0 and 7

    // Give the answer
    cout << "Magic 8-Ball says: " << answers[randomIndex] << endl;

    return 0; // End the program
}
