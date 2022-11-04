todo = []

choose = " "


def menu():
    print("1 - Add a new task")
    print("2 - Remove a task")
    print("3 - Show ToDo")
    print("4 - Exit")


while choose != 4:
    menu()
    choose = int(input("Choose the action: "))

    if choose == 1:
        i = input("Add a new task: ")
        todo.append(i)
        print("Added: " + i)
    elif choose == 2:
        i = input("Task to remove: ")
        if i in todo:
            todo.remove(i)
            print("Removed: " + i)
        else:
            print("Task doesn't exist")
    elif choose == 3:
        print(todo)
    elif choose == 4:
        print("Good Bye")
