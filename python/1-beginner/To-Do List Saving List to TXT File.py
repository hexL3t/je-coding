# Simple To-Do List Program with File Storage

# Function to load tasks from the file
# This function reads the saved tasks from the 'tasks.txt' file and returns them as a list.
def load_tasks():
    try:
        # Open the tasks file in read mode
        with open("tasks.txt", "r") as file:
            # Read all lines, strip any leading/trailing whitespace, and return as a list
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        # If the file does not exist, return an empty list
        return []

# Function to save tasks to the file
# This function writes the tasks from the 'tasks' list to the 'tasks.txt' file.
def save_tasks():
    # Open the tasks file in write mode (this will overwrite the file)
    with open("tasks.txt", "w") as file:
        # Loop through the tasks and write each one to the file
        for task in tasks:
            file.write(task + "\n")

# Load existing tasks when the program starts
# This loads any previously saved tasks from the file so the user doesn't lose them when the program ends
tasks = load_tasks()

# Function to add a new task
# This function takes a task (string) as input, adds it to the task list, and saves the list to the file.
def add_task(task):
    tasks.append(task)  # Add the task to the list
    save_tasks()  # Save the updated list to the file
    print(f"Task '{task}' added successfully!")  # Provide feedback to the user

# Function to view all tasks
# This function displays all tasks in the list to the user
def view_tasks():
    if tasks:
        # If there are tasks, display them with their index number
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):  # Start counting from 1 for a user-friendly list
            print(f"{index}. {task}")  # Display each task with its number
    else:
        # If no tasks are present, inform the user
        print("Your to-do list is empty.")

# Function to remove a task
# This function removes a task by its index number and saves the updated list
def remove_task(index):
    # Check if the index is within the valid range of tasks
    if 1 <= index <= len(tasks):
        # Remove the task at the specified index (adjusted for 1-based index)
        removed_task = tasks.pop(index - 1)
        save_tasks()  # Save the updated list to the file
        print(f"Task '{removed_task}' removed successfully!")  # Provide feedback to the user
    else:
        # If the index is invalid, notify the user
        print("Invalid task number.")

# Main program loop
# This is the part of the program that continuously runs, asking the user for input and processing it.
while True:
    # Display the menu options to the user
    print("\n--- To-Do List Menu ---")
    print("1. Add a task")  # Option to add a new task
    print("2. View tasks")  # Option to view all tasks
    print("3. Remove a task")  # Option to remove an existing task
    print("4. Quit")  # Option to quit the program
    
    # Get the user's choice from the menu
    choice = input("Enter your choice (1-4): ")
    
    # Process the user's choice
    if choice == '1':
        task = input("Enter the task: ")  # Ask for the task description
        add_task(task)  # Call the function to add the task
    elif choice == '2':
        view_tasks()  # Call the function to view all tasks
    elif choice == '3':
        view_tasks()  # Display the tasks before removing one
        if tasks:  # Check if there are any tasks to remove
            # Ask the user for the task number they want to remove
            index = int(input("Enter the number of the task to remove: "))
            remove_task(index)  # Call the function to remove the task
    elif choice == '4':
        print("Thank you for using the To-Do List program. Goodbye!")  # Thank the user and exit
        break  # Exit the loop, ending the program
    else:
        # If the user enters an invalid option, notify them
        print("Invalid choice. Please try again.")
