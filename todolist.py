tasks = []
def show_menu():
    print("TO-DO LIST MENU")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
def view_tasks():
    if not tasks:
        print("\nYour task list is empty!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
def add_task():
    new_task = input("\nEnter a new task: ")
    tasks.append(new_task)
    print("Task added successfully!")
def update_task():
    view_tasks()
    if tasks:
        try:
            task_no = int(input("\nEnter task number to update: "))
            if 1 <= task_no <= len(tasks):
                new_text = input("Enter updated task: ")
                tasks[task_no - 1] = new_text
                print("Task updated!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")
def delete_task():
    view_tasks()
    if tasks:
        try:
            task_no = int(input("\nEnter task number to delete: "))
            if 1 <= task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"Task '{removed}' deleted!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")
while True:
    show_menu()
    choice = input("\nChoose an option (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please enter again.")
