# Project: Simple Calculator
# For this project, you will create a Python program that can perform basic arithmetic operations (addition, subtraction, multiplication, and division) based on user input.
# The program should have the following features:

# Function Definition
# Define a Python function called calculator that takes three arguments: two numbers (num1 and num2) and an operator (operator).
#Inside the function, implement the logic to perform the specified operation based on the operator.

# Operation Implementation
# Add code inside the calculator function to handle each of the four basic operations:
# 	Addition (+)
# 	Subtraction (-)
#	Multiplication (*)
# Division (/)

# Use conditional statements (if, elif, else) to check the operator and perform the corresponding calculation.
# Return the result of the calculation.

# Error Handling
# Include an else block to handle invalid operators entered by the user.
# Print an appropriate error message if an invalid operator is provided.

# User Input
# Create a loop that repeatedly prompts the user to enter two numbers and an operator.
# Call the calculator function with the user's input and store the result.
# Print the result of the calculation.

# Program Exit
# Add a condition to the loop that allows the user to exit the program by entering a specific value (e.g., 'q' for quit).

# Testing
# Test your program with different inputs, including valid and invalid operators, to ensure it works correctly.
# Verify that the program handles division by zero gracefully (e.g., by printing an error message or using exception handling).

# This project will help you practice various aspects of Python programming, such as function creation, conditional statements, loops, and user input handling. You can enhance the project further by adding more features, such as support for more complex operations or a graphical user interface (GUI).
# Remember to break down the project into smaller steps and tackle each step one by one. If you get stuck, refer to Python documentation, online tutorials, or ask for assistance from your instructor or peers.
# Good luck with your project!


def calculator (num1, num2, operator):
    # Create function so that it takes num1, num2 and operator.
    # Use of an If-Else statement may be useful.
    
while True:
    # Use a try-except loop here.
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    # Have an exit message
    # Print an error statement using ValueError as the except function.
    
