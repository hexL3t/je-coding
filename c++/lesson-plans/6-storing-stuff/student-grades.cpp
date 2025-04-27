// Student Grades Tracker (Array with Names and Grades)
/* What it does:
   * Takes input for the names of 5 students.
   * Takes input for their grades.
   * Displays each student’s name with their grade.
   * Calculates and displays the average grade for all students. */

#include <iostream>  // This allows us to use input and output
using namespace std;

int main() {
    // Array of student names (5 students)
    string students[5] = {"Student 1", "Student 2", "Student 3", "Student 4", "Student 5"};
    
    // Array to store the grades of 5 students
    double grades[5];
    
    // Variable to calculate the total sum of all grades
    double total = 0.0;
    
    cout << "Enter grades for 5 students:" << endl;
    
    // Loop to take input for each student's grade
    for (int i = 0; i < 5; i++) {
        cout << "Enter grade for " << students[i] << ": ";
        cin >> grades[i];  // Take input for each student's grade
        total += grades[i]; // Add the grade to the total sum
    }

    cout << endl << "=== Student Grades ===" << endl;

    // Loop to display each student's name and grade
    for (int i = 0; i < 5; i++) {
        cout << students[i] << ": " << grades[i] << endl;
    }

    // Calculate the average grade
    double average = total / 5;

    cout << endl << "The average grade is: " << average << endl;

    return 0;  // End of the program
}

/* What Happens in This Program?
    Arrays for Student Names and Grades:
        students[5] stores the names of 5 students.
        grades[5] stores the grades of the 5 students.

    User Input:
        The program asks the user to input the grades for each student one by one.
        We store each grade in the grades array.

    Total and Average:
        We calculate the total sum of all the grades by adding each grade to a variable called total.
        Then, we calculate the average by dividing the total by 5 (the number of students).

    Display Information:
        The program displays each student's name along with their grade.
        It also displays the average grade for all students.
*/
