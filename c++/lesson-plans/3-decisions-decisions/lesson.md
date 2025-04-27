# 🤔 Lesson 3: Decisions, Decisions!
## 🎯 Lesson Goal
Learn how to make your program think with conditions and decisions!

## 🧠 What is Conditional Logic?
* Sometimes, a program needs to choose what to do.
* We use if and else to help the computer make decisions.

## 🧾 Comparison Operators
| Operator      | Meaning                  | Example  ( x = 5 )   |
|:-------------:| -------------            | -------------        |
| ``` == ```    | Is Equal To              | ```x == 5 is TRUE``` |
| ``` != ```    | Is **NOT** Equal To      | ```x != 3 is TRUE``` |
| ``` >  ```    | Greater Than             | ```x > 3 is TRUE```  |
| ``` <  ```    | Less Than                | ```x < 10 is TRUE``` |
| ``` >= ```    | Greater Than or Equal To | ```x >= 5 is TRUE``` |
| ``` <= ```    | Less Than or Equal To    | ```x <= 6 is TRUE``` |

## 🕹️ Mini Project: Guess the Secret Number
Can your code tell if someone guessed the right number?
```c++
#include <iostream>
using namespace std;

int main() {
	int guess;
	int secret = 7;

	cout << "Guess the secret number (1–10): ";
	cin >> guess;

	if (guess == secret) {
    	cout << "You got it right!" << endl;
	} else {
    	cout << "Oops! Try again." << endl;
	}

	return 0;
}
```

### ✍️ Task:
Change the secret number or add more hints to make your game more fun!

### ✏️ Student Worksheet: Draw the Logic
Activity: Draw a flowchart for this guessing game!

#### 🧩 Use these blocks:
* Start
* Ask for guess
* Compare guess == secret
* Show "Correct!" OR "Try again"
* End
  
🖍️ Students can use arrows and shapes to design the decision path.

### ✅ Student Worksheet: True or False?
Write T for True or F for False:
| Statement                                       | Answer        |
| -------------                                   | ------------- | 
| if ```x == 10 ``` checks if x is exactly 10  .  |               | 
| else is only used when somethnig is true .      |               | 
| A program can decide what to do using if.       |               | 
| == and = mean the same thing.                   |               |  
| if ```(guess != 7)``` means the guess is not 7. |               | 