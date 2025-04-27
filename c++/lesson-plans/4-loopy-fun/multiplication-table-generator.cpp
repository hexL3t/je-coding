// === Multiplication Table Generator! ✖️ ===
// In this project, we learn:
// - How to use loops inside other loops (nested loops)
// - How to format output to make a table

#include <iostream> // For input and output
using namespace std; // No need for "std::" every time

int main() {
    int size;

    // Ask the user how big they want the table
    cout << "Enter the size of the multiplication table: ";
    cin >> size;

    cout << "Here’s your " << size << "x" << size << " multiplication table!" << endl;

    // Outer loop for rows
    for (int i = 1; i <= size; i++) {
        // Inner loop for columns
        for (int j = 1; j <= size; j++) {
            cout << i * j << "\t"; // \t makes a tab space for nice formatting
        }
        cout << endl; // Start a new line after each row
    }

    return 0; // End the program
}
