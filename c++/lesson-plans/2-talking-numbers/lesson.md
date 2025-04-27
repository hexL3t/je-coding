# 🧮 Lesson 2: Talking Numbers
## 🎯 Lesson Goal
Learn how to use variables, accept user input, and do basic math in C++!
## 🔢 What's a Variable?
A variable is like a box that holds a value.
| Data Type     | What it stores     | Example               |
| ------------- | -------------      | -------------         |
| ``` int ```   | Whole Numbers      | ```7```, ```42```     |
| ``` float ``` | Decimal Numbers    | ```3.14```, ```9.8``` |
| ``` char ```  | Single Characters  | ```A```, ```z```      |

## 👂 Getting Input from the User

```c++
cin >> variableName;
```
* Think of cin as “C++ Input”
* It lets the user type in a value
* That value is saved inside the variable

## 💬 Talking Back with Output
```c++
cout << "Text or variable";
```
* cout is “C++ Output”
* It shows text or values on the screen
* Use << to send info to the screen

## ➕ Let’s Do Some Math!
Math in C++ is just like regular math!
| Operator      | Meaning       | Example         |
| ------------- | ------------- | -------------   |
| ``` + ```     | Add           | ```3 + 2 = 5``` |
| ``` - ```     | Subtract      | ```5 - 1 = 4``` |
| ``` * ```     | Multiply      | ```2 * 4 = 8``` |
| ``` / ```     | Divide        | ```8 / 4 = 2``` |

## 🐾 Mini Project: Pet Age Calculator
Let’s figure out how old your pet would be in human years!
``` c++
#include <iostream>
using namespace std;

int main() {
	int petAge;
	cout << "Enter your pet's age: ";
	cin >> petAge;
	int humanAge = petAge * 7;
	cout << "That's about " << humanAge << " in human years!" << endl;
	return 0;
}
```
### ✍️ Your Turn:
Try changing the pet age or the multiplier to explore different types of pets!

### ✏️ Student Worksheet: Data Type Match-Up
Match the variable to the correct type:
| Variable             | Value Example | Data Type (```int```/```float```/```char```) |
| -------------        | ------------- | -------------                                |
| ``` age ```          | ```10```      |                                              |
| ``` gradeAverage ``` | ```87.5```    |                                              |
| ``` initial ```      | ```'B'```     |                                              |

### ✏️ Student Worksheet: Fill In the Code
Fill in the blanks to complete your own pet age calculator:
``` c++
#include <__________>
using namespace _______;

int main() {
	int petAge;
	cout << "Enter your pet's age: ";
	cin >> _______;
	int humanAge = petAge * ___;
	cout << "That's about " << humanAge << " in human years!" << endl;
	return ___;
}
```

### 📐 Student Worksheet: Solve and Code
Math Time!
1. If a pet is 5 years old, how old is it in human years (×7)?

   Answer: _______
2. Write a line of C++ code that shows the result:
``` c++
cout << "Your pet is ________ in human years!" << endl;
```
