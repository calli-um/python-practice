print("TO-DO LIST")
taskList = []

def validate(choice):
    while True:
        if choice == 'y' or choice == 'n':
            return choice
        else:
            print("Enter y or n only.")
            choice = input().lower()

def addTask():
    while True:
        print(f'Enter task {len(taskList)+1}:')
        task = input()
        taskList.append(task)
        choice = input("Add another task? (y/n): ").lower()
        ans = validate(choice)
        if ans == 'n':
            break

def viewTasks():
    for index in range(0, len(taskList)):
        print(f'{index+1}: {taskList[index]}')

def deleteTask():
    if not taskList:
        print("No tasks to delete.")
        return
    while True:
        print("1. Delete by Task Number")
        print("2. Delete by Task Name")
        choice = input("Enter your choice: ")
        if choice == '1':
            try:
                print("Enter task number to delete: ")
                num = input()
                num = int(num)
                if 1 <= num <= len(taskList):
                    removed = taskList.pop(num - 1)
                    print(f"Task '{removed}' removed.")
                else:
                    print("Invalid task number.")
            except:
                print("Please enter a valid number.")
        elif choice == '2':
            name = input("Enter exact task name to delete: ")
            if name in taskList:
                taskList.remove(name)
                print(f"Task '{name}' removed.")
            else:
                print("Task not found.")
        else:
            print("Invalid option.")
        choice = input("Delete another task? (y/n): ").lower()
        ans = validate(choice)
        if ans == 'n':
            break  

def MainMenu():
    while True:
        print("Features:")
        print("1.Add new task \n2.Show all tasks \n3.Remove a task \n4.Exit")
        print("Enter your choice: (1-4)")
        choice = input()
        choice = str(choice)
        if choice == '1':
            addTask()
        elif choice == '2':
            viewTasks()
        elif choice == '3':
            deleteTask()
        elif choice == '4':
            print('Thank you. Exiting...')
            break
        else:
            print('Invalid choice. Enter again: (1-4)')

MainMenu()
