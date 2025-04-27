#include <iostream>  // This lets us use input and output functions
using namespace std;

int main() {
    // This is an array of 5 snacks (strings), like a list of favorite snacks.
    string snacks[5] = {"Chips", "Chocolate", "Fruit", "Popcorn", "Cookies"};

    cout << "My top 5 snacks are:" << endl;  // Print a title for the list

    // This is a "for" loop that goes through each snack in the array and prints it.
    for (int i = 0; i < 5; i++) {
        // Print the number (i+1) followed by the snack name
        cout << i+1 << ". " << snacks[i] << endl;
    }
    
    return 0;  // End of the program
}
