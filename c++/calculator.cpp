// Calculator is a beginner project, introducing user input,
// basic arithmetic operations, and conditional statements.

#include <iostream> // IO Stream Library for Input and Output Operations ** Mandatory

using namespace std;    // namespace std = Standard Functionality (std::)

int main(){
    double num1, num2;      // Variable for decimal numbers(integers).
    char operation;         // Variable for Character (+, -, /, *)

     // Takes input from the user for the numbers and the arithmetic operation.
    cout << "Enter first number: ";
    cin >> num1;

    cout << "Enter second number: ";
    cin >> num2;

    cout << "Enter an operation (+, -, *, /): ";
    cin >> operation;

    // switch(operation){..} : decision-making statement to exucute different code based on 
    // the 'operation' chosen.
    switch(operation){
        case '+':
            cout << "Result: " << num1 + num2 << endl;
            break;
        case '-':
            cout << "Result: " << num1 - num2 << endl;
            break;
        case '*':
            cout << "Result: " << num1 * num2 << endl;
            break;
        case '/':
            if (num1 != 0 || num2 != 0)
            {
                cout << "Result: " << num1 / num2 << endl;
            }
            else 
            {
                cout << "Error: Division by zero" << endl;
            }
            break;
        default: 
            cout << "Error: Invalid Operation" << endl;
    }
    return 0;   
}