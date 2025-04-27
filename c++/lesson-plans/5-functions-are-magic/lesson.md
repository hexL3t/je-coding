# 🧙‍♂️ Lesson 5: Functions Are Magic
## 🎯 Lesson Goal
Learn how to break up your code into reusable blocks called functions!

## 🔧 What is a Function?
A function is like a magic box that does a specific job and can be used anytime you need it!

### 📝 Parts of a Function
* Declaration: We tell the program about the function and what it does.
  * It has a name, input parameters, and a return type (what the function will return).
* Call: We tell the program to use the function whenever we need it.
* Return: A function can give back a result that can be used later in the program.

## 🔑 Syntax of a Function
``` c++
returnType functionName(parameters) {
	// Code that does the work
	return value;  // Optional, if we need to return something
}
```

## ✨ Mini Project: Build-a-Compliment
We’re going to create a program that gives a fun compliment based on the user's name.
``` cpp
#include <iostream>
using namespace std;

// Function declaration
string compliment(string name) {
	return "You're awesome, " + name + "!";
}

int main() {
	string yourName;
	cout << "What's your name? ";
	cin >> yourName;
	cout << compliment(yourName) << endl;  // Function call
	return 0;
}
```

### ✏️ Student Worksheet: Label the Parts of a Function
Activity: Label the parts of the function below.
```cpp
___________ greet(string name) {
	___________ "Hello, " + name + "!";
    return 0;
}
```
| ```code```                                 | Labels to Match      |
| ------------                               | -------------        | 
| ```___________ greet(string name) {```     |  1. Return Type      | 
| ```___________ "Hello, " + name + "!";```  |  2. Function Name    | 
| ```return 0;```                            |  3. Parameters       | 
| ```}```                                    |  4. Return Statement |  

### ✏️ Student Worksheet: Create Your Own Compliment Function
Write a function that returns a unique compliment for the user!
```cpp
__________ compliment(string name) {
	__________ "You're a rockstar, " + name + "!";
    return 0;
}
```
#### Hints:
* The return type is string
* Use your imagination to make it fun!.

## 🌟 Extension Activity: Compliment Expansion
* Create a function that takes two parameters (name and favorite color) and returns a compliment like: "You look amazing in color!"
* Introduce the idea of void functions (functions that don’t return a value), like a function that simply prints a message without returning anything.
