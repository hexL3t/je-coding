# 📦 Lesson 6: Storing Stuff — Arrays
## 🎯 Lesson Goal
Learn how to use arrays to store multiple values in one place!

## 🧳 What is an Array?
* An array is like a container that holds multiple values of the same type. 
* For example, an array could hold your favorite snacks or your test scores!

We learnt about lists briefly last lesson, an array is what we call lists in C++!
## 📝 How to Use an Array
Declare an Array: You need to specify the number of items the array will hold and the type of items.

``` c++
dataType arrayName[arraySize] = {value1, value2, ..., valueN};
```
```Access Elements:``` Each item in an array has an index (a number showing its position).
The first element is at index 0, the second at index 1, and so on.

## ✨ Mini Project: Top 5 Snacks
We’ll create a program that stores your top 5 favorite snacks in an array and prints them one by one!
``` cpp
#include <iostream>
using namespace std;

int main() {
	// Array of top 5 snacks
	string snacks[5] = {"Chips", "Chocolate", "Fruit", "Popcorn", "Cookies"};

	cout << "My top 5 snacks are:" << endl;
	// Loop through array and print each snack
	for (int i = 0; i < 5; i++) {
    	cout << i+1 << ". " << snacks[i] << endl;
	}
    
	return 0;
}
```

### ✏️ Student Worksheet: Draw the Array 
Activity: Draw an array with boxes to represent your top 5 snacks! 
Label each box with a snack from the list:
|                    |                         |
| :------------:     | -------------           | 
| ```Box 1```        |  ____________________   | 
| ```Box 2```        |  ____________________   | 
| ```Box 3```        |  ____________________   | 
| ```Box 4```        |  ____________________   |  
| ```Box 5```        |  ____________________   | 

### ✏️ Student Worksheet: Match Code with Array Values
Match the code below with the correct snack name.
| ```code```        | snack                   |
| :------------:    | -------------           | 
| ```snacks[0]```   |  ____________________   | 
| ```snacks[1]```   |  ____________________   | 
| ```snacks[2]```   |  ____________________   | 
| ```snacks[3]```   |  ____________________   |  
| ```snacks[40]```  |  ____________________   | 

## 🌟 Extension Activity: Compliment Expansion
* Modify the program to allow users to input their own snacks.
* Change the array size to 10 and store 10 snacks instead of just 5.