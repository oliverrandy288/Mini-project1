import sys

# Task list
tasks = []

def print_welcome_message():
    """Print the welcome message and menu options."""
    print("Welcome to the To-Do List App!")
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task():
    """Add a new task to the list."""
    try:
        title = input("Enter the task title: ").strip()
        if not title:
            raise ValueError("Task title cannot be empty.")
        tasks.append({"title": title, "status": "Incomplete"})
        print(f"Task '{title}' added.")
    except ValueError as e:
        print(f"Error: {e}")

def view_tasks():
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks available.")
        return
    
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task['title']} - {task['status']}")

def mark_task_complete():
    """Mark a specified task as complete."""
    try:
        view_tasks()
        task_number = int(input("Enter the number of the task to mark as complete: "))
        if not (1 <= task_number <= len(tasks)):
            raise IndexError("Task number out of range.")
        tasks[task_number - 1]['status'] = 'Complete'
        print(f"Task '{tasks[task_number - 1]['title']}' marked as complete.")
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

def delete_task():
    """Delete a specified task from the list."""
    try:
        view_tasks()
        task_number = int(input("Enter the number of the task to delete: "))
        if not (1 <= task_number <= len(tasks)):
            raise IndexError("Task number out of range.")
        deleted_task = tasks.pop(task_number - 1)
        print(f"Task '{deleted_task['title']}' deleted.")
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

def main():
    """Main function to run the To-Do List application."""
    while True:
        print_welcome_message()
        try:
            choice = int(input("Select an option (1-5): "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                mark_task_complete()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print("Quitting the application. Goodbye!")
                break
            else:
                print("Invalid option. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        finally:
            print("-" * 40)

if __name__ == "__main__":
    main()
