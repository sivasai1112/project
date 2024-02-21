# Define an empty list to store tasks
tasks = []

# Function to display the to-do list
def display_todo_list():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["status"] else "Not Done"
            print(f"{i}. {task['name']} ({status})")

# Function to add a task to the to-do list
def add_task(task_name):
    tasks.append({"name": task_name, "status": False})
    print(f"Task '{task_name}' added to your to-do list.")

# Function to mark a task as completed
def mark_task_completed(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["status"] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Function to remove a task from the to-do list
def remove_task(task_number):
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['name']}' removed from your to-do list.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Display To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Completed")
    print("4. Remove a Task")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_todo_list()
    elif choice == '2':
        task_name = input("Enter the task: ")
        add_task(task_name)
    elif choice == '3':
        display_todo_list()
        task_number = int(input("Enter the task number to mark as completed: "))
        mark_task_completed(task_number)
    elif choice == '4':
        display_todo_list()
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
