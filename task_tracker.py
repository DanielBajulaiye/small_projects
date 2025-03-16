import os

TASKS_FILE = "tasks.txt"

tasks = []
if os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]




while True:
    print("\n To-Do List Menu:")
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Remove a Task")
    print("4. Quit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter your task")
        tasks.append(task)
        print(f"Task added: {task}")
    elif choice == "2":
        if not tasks:
            print(" No tasks yet!.")
        else:
            print("\n Your To-Do List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {tasks}")
    elif choice == "3":
        if not task:
            print("There's no task to be removed")
        else:
            print("\n Remove a Task:")
            for index, task in enumerate(tasks, start = 1):
                print(f"{index}. {task}")

            try:
                task_number = int(input("Enter the number of the task to remove:"))
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Task removed:{removed_task}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print(" Please enter a valid number.")
        print("You chose to remove a task")
    elif choice == "4":
        with open(TASKS_FILE, "w") as file:
            for task in tasks:
                file.write(task + "\n")

        print("Tasks saved.Goodbye!")
        break
    else:
        print("Invalid choice, please enter 1-4.")