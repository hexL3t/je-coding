# 📝 What is a ```list```?
In programming, a list is a collection of items stored together. Each item in a list has a position or index, which allows us to access them easily. You can think of a list like a box that holds many things, and you can pick any item from the box based on its position.

### 📋 Examples of Lists:
* A shopping list of things you need to buy.
* A playlist of songs to listen to.
* A to-do list of tasks to complete.

### In programming:
Lists can hold different types of data: numbers, words (strings), or even more lists!

Each item in the list can be accessed by its index (position in the list).

## 🔢 Example 1: A List of Numbers
Imagine you have a list of the numbers 1, 2, and 3. 

The list looks like this:
``` cpp
[1, 2, 3]
```
* The first item is 1, the second item is 2, and the third item is 3.
* In programming, the index starts at 0, so:
  * Index 0: 1
  * Index 1: 2
  * Index 2: 3

## 🛒 Example 2: A List of Words
Now imagine you have a list of words:
``` cpp
["apple", "banana", "cherry"]
```
* Index 0: "apple"
* Index 1: "banana"
* Index 2: "cherry"

## ✅ How Do We Use Lists in Code?
Let’s see a C++ example using a list (called an array in C++):
``` cpp
#include <iostream>
using namespace std;

int main() {
    // A list (array) of 3 numbers
    int numbers[] = {1, 2, 3};

    // Accessing each number in the list using its index
    cout << "First number: " << numbers[0] << endl;  // prints 1
    cout << "Second number: " << numbers[1] << endl; // prints 2
    cout << "Third number: " << numbers[2] << endl;  // prints 3

    return 0;
}
```
### Key Points:
* The list ```numbers[]``` holds three numbers: 1, 2, and 3.
* We use indexing (e.g., ```numbers[0]```, ```numbers[1]```, etc.) to access each item in the list.

## What Can You Do with a List?
* You can ```store a lot of items``` in one variable, so you don't need to create multiple separate variables.
* You can ```loop through``` a list to work with each item (for example, add all numbers together, or print each word).
* You can ```change the items``` in a list later if needed.