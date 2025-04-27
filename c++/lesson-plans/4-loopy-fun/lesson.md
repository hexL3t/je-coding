# 🔄 Lesson 4: Loopy Fun
## 🎯 Lesson Goal
Learn how to use loops to make our programs repeat tasks!

## 🔁 What Are Loops?
A loop is a way to repeat an action many times without writing the same code again.
## 📝 Types of Loops
* ```for``` loop: When you know how many times to repeat something.
	Syntax:
``` c++ 
for (initialization; condition; update) {
	// code to repeat
}
```

* ```while``` loop: When you repeat as long as a condition is true.
	Syntax:
``` c++ 
while (condition) {
	// code to repeat
}
```

* ```do-while``` loop: Like while, but the code runs at least once, even if the condition is false.
	Syntax:
``` c++ 
do {
	// code to repeat
} while (condition);
```

## 🚀 Mini Project: Countdown Rocket
We’re going to write a program that counts down from 10, then prints "Lift off!"
``` c++ 
#include <iostream>
using namespace std;

int main() {
	for (int i = 10; i > 0; i--) {
    	cout << i << "..." << endl;
	}
	cout << "Lift off!" << endl;
	return 0;
}
```

## ✏️ Student Worksheet: Fill in the Code
Complete the Countdown Code!
``` c++ 
#include <__________>
using namespace _______;

int main() {
	for (int i = ___; i > ___; i--) {
    	cout << i << "..." << endl;
	}
	cout << "Lift off!" << endl;
	return ___;
}
```
### 🔍 Student Worksheet: Trace the Loop
Follow the loop as it runs. Write down the output of each iteration.
| ```i value```  | Answer        |
| :------------: | ------------- | 
| ```10```       |  __________   | 
| ```9```        |  __________   | 
| ```8```        |  __________   | 
| ```7```        |  __________   |  
| ```6```        |  __________   | 
| ```5```        |  __________   | 
| ```4```        |  __________   | 
| ```3```        |  __________   | 
| ```2```        |  __________   |  
| ```1```        |  __________   | 


## 🌟 Extended Activity: Rocket Countdown Challenge
* Add sound effects (like ```Whoosh!``` or ```Blastoff!```) after each countdown number.
* Experiment with the while loop by replacing the for loop and seeing the differences.


