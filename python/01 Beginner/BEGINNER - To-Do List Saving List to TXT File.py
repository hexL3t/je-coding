# Simple To-Do List Program with File Storage

# Function to load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Function to save tasks to file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Load existing tasks
tasks = load_tasks()

# Function to add a task
def add_task(task):
    tasks.append(task)
    save_tasks()
    print(f"Task '{task}' added successfully!")

# Function to view all tasks
def view_tasks():
    if tasks:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty.")

# Function to remove a task
def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks()
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task number.")

# Main program loop
while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        if tasks:
            index = int(input("Enter the number of the task to remove: "))
            remove_task(index)
    elif choice == '4':
        print("Thank you for using the To-Do List program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")