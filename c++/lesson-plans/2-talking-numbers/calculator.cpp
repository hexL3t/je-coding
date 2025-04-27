// === Basic Calculator Project ===
// This project introduces:
// - User input (getting numbers from the player)
// - Basic math (addition, subtraction, multiplication, division)
// - Conditional logic (deciding what to do based on the user's choice)

#include <iostream> // Needed for input (cin) and output (cout)
using namespace std; // So we don't have to type "std::" every time

int main() {
    double num1, num2; // Boxes (variables) to hold the two numbers (decimals or integers)
    char operation;    // A box to hold the math operation (+, -, *, /)

    // Ask the user for the first number
    cout << "Enter first number: ";
    cin >> num1; // Save what they type into num1

    // Ask the user for the second number
    cout << "Enter second number: ";
    cin >> num2; // Save what they type into num2

    // Ask the user which operation they want to do
    cout << "Enter an operation (+, -, *, /): ";
    cin >> operation; // Save the operation they choose

    // Now decide what to do based on the operation
    switch(operation) {
        case '+':
            cout << "Result: " << num1 + num2 << endl; // Add the numbers
            break;
        case '-':
            cout << "Result: " << num1 - num2 << endl; // Subtract the numbers
            break;
        case '*':
            cout << "Result: " << num1 * num2 << endl; // Multiply the numbers
            break;
        case '/':
            if (num2 != 0) { // Make sure we're not dividing by zero!
                cout << "Result: " << num1 / num2 << endl; // Divide the numbers
            } else {
                cout << "Error: Cannot divide by zero!" << endl; // Show an error
            }
            break;
        default:
            cout << "Error: Invalid Operation" << endl; // If they didn't type +, -, *, or /
    }

    return 0; // End the program
}

/*
How the Calculator Works:
1. The program asks for two numbers.
2. The player chooses a math operation (+, -, *, /).
3. The program solves the math problem and shows the answer!

💡 Feel free to add even more operations (like squaring a number, or using exponents!)
*/