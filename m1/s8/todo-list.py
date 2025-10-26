# global variable
todo_list = []
option = 0


def add_task(task: str):
    todo_list.append(task)
    print("Task added successfully!")


def remove_task(task: str):
    todo_list.remove(task)
    print("Task removed successfully!")


# main logic
while option != 99:
    print("1.) Add Task")
    print("2.) Remove Task")
    print("99.) Exit Program")
    option = int(input("Select an option: "))

    if option == 1:
        task = input("Enter a new task: ")
        if task in todo_list:
            print("Task already exists!")
        else:
            add_task(task)
            print(todo_list)
    elif option == 2:
        task = input("Enter a task to remove: ")
        if task not in todo_list:
            print("Task not found!")
        else:
            remove_task(task)
            print(todo_list)
    else:
        break
