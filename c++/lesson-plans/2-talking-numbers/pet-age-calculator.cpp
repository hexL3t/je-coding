#include <iostream> // This lets us use input (cin) and output (cout) in our program
using namespace std; // This saves us from typing "std::" every time we use cin or cout

int main() { // This is where the program starts running
    int petAge; // We create a box (called a "variable") to store the pet's age

    cout << "Enter your pet's age: "; // Ask the user to type their pet's age
    cin >> petAge; // Save the number the user types into the petAge box

    int humanAge = petAge * 7; // Calculate the "human years" by multiplying by 7

    cout << "That's about " << humanAge << " in human years!" << endl; 
    // Show the user the answer!

    return 0; // End of the program
}
