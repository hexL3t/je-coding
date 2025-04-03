#include <iostream>     // preprocessor directive: Input/Output Stream Library
// #include string         // access to String Library (simplify std::string )

using namespace std;    // 'std' acronym for ' Standard' and Namespace = built-in functionality

// Function to demonstrate variables and data types
void variablesDemo() {
    int integerVar = 10;                // Integer : Whole Number (0, 1, 10, 20)
    double doubleVar = 20.5;            // Floating Point : Decimals
    char charVar = 'T';                 // Char : Character
    string stringVar = "Hello, C++!";   // String : Words/Sentence
    bool booleanVar = true;             // Boolean : True/False (0,1)

    cout << "Integer: " << integerVar << endl;  // endl = end line; moves cursor to the next line in console (output)
    cout << "Double: " << doubleVar << endl;
    cout << "Character: " << charVar << endl;
    cout << "String: " << stringVar << endl;
    cout << "Boolean: " << booleanVar << endl;
}

// Main Function
int main() {
    cout << "=== Welcome to the C++ Basics Tutorial! ===";

    // Demonstrating Varaibles
    cout << "====== Demonstrating Varaibles ======" << endl;
    variablesDemo();

} 