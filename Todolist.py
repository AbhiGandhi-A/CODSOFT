tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(task):
    try:
        tasks.remove(task)
        print(f"Task '{task}' removed.")
    except ValueError:
        print(f"Task '{task}' not found in the list.")

def show_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks in the list.")

def clear_tasks():
    global tasks
    tasks = []
    print("All tasks cleared.")

def main():
    while True:
        print("\n===== TO-DO LIST MANAGER =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Clear All Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter task to add: ")
            add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            remove_task(task)
        elif choice == '3':
            show_tasks()
        elif choice == '4':
            clear_tasks()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()

