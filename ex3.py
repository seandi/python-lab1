
input_string = """Insert the number corresponding to the action you want to perform:
1. insert a new task;
2. remove a task;
3. show all the tasks;
4. close the program.
Your choice: """
task_list = []
while True:
    try:
        choice = int(input(input_string))
        if choice == 1:
            task = input("Type new task: ")
            task_list.append(task)
        elif choice == 2:
            task = input("Type task to remove: ")
            task_list.remove(task)
        elif choice == 3:
            print("Printing list of task to do:")
            print(task_list)
        elif choice == 4:
            print("Terminating")
            break
        else:
            print("Invalid choice")
            continue
    except ValueError:
        print("Input should be an integer")
        continue
