# To-Do List Application

tasks = []  # Global list to store tasks

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour TO-DO LIST:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def update_task():
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to update: "))
        if 0 < task_num <= len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[task_num - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
