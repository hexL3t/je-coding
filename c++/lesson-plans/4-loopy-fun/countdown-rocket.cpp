// === Rocket Launch Countdown! 🚀 ===
// In this mini project, we learn:
// - How to use a "for loop" to repeat something
// - How to count DOWN from a number

#include <iostream> // Needed for input and output
using namespace std; // So we don't need to type "std::" every time

int main() {
    // For loop to count down from 10 to 1
    for (int i = 10; i > 0; i--) {
        cout << i << "..." << endl; // Print the current number followed by "..."
    }

    // After the countdown finishes, print "Lift off!"
    cout << "Lift off!" << endl;

    return 0; // End the program
}
