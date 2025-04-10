/*
== TO DO LIST ==
A step into the real world since you’ll be building a tool you can actually use every day!

Covering:
    - file handling
    - basic data management
    - practical introduction to managing and persisting data

These are foundational skills for any C++ programmer, and it’s the ideal time to move from simple 
input/output to storing data persistently. 

*/

#include <iostream>
#include <fstream>  // File Streams: provides classes for reading and writing into files or data streams
#include <vector>   // Vector : Library that has many functions that allow you to perform tasks on vectors
#include <string>   // String: Library that has many functions that allow you to perform tasks on strings. 

using namespace std;

// Function to display tasks in the to-do list
void showTasks(const vector<string> &tasks){
    
    // Display the header for the to-do list
    cout << " === TO DO LIST ===" << endl;

    // Loop through each task and print it with its index (starting from 1)
    for(int i = 0; i < tasks.size(); ++i){
        // Printing the task number (index + 1) followed by the task itself
        cout << i + 1 << ". " << tasks[i] << endl; // Printing the numbers next to task (eg. "1. Task Name")
    }
}

int main() {
    vector<string> tasks;    // Vector to store task names
    string task;             // String to temporarily hold a task name
    char choice;             // Variable to hold the user's choice

    // Load existing tasks from the file "tasks.txt"
    ifstream inputFile("tasks.txt");        // Open file for reading

    // Read each line of the file and add it to the tasks vector
    while (getline(inputFile, task)){
        tasks.push_back(task);  // Add each task to the tasks vector
    }
    inputFile.close();       // Close the file after reading

    // Start the main program loop
    do {
        // Display the menu options for the user
        cout << "[A] Add a Task" << endl;
        cout << "[V] View Tasks" << endl;
        cout << "[Q] Quit" << endl;

        // Get the user's choice
        cout << "Enter your choice: ";
        cin >> choice;

        // Handle the user's menu choice
        switch(choice){
            case 'A':
            case 'a':
                std::cout << "== Enter a Neaw Task ==" << endl;
                std::cout << "Enter Task: ";
                cin.ignore(); // Clears the input buffer to prevent issues with getline()
                getline(cin, task);     // Get the task input from the user
                tasks.push_back(task);  // Add the new task to the vector
                break;
            case 'V':
            case 'v':
                cout << "== Current Task List ==" << endl;
                showTasks(tasks); // Call the showTasks function to display all tasks
                break;
            case 'Q':
            case 'q':
                cout << "Saved..." << endl;
                break;
            default:
                cout << "Error: Invalid." << endl;
        }
    } while (choice != 'Q' && choice != 'q'); // Continue looping until the user chooses to quit

    // Save the tasks to the file before exiting
    ofstream outputFile("tasks.txt"); // Open file for writing
    
    // Loop through all tasks in the vector
    for (const auto &t : tasks){
        outputFile << t << endl; // Write each task to the file
    }
    outputFile.close(); // Close the file after writing

    return 0;
}