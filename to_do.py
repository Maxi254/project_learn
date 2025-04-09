user_list = []

while True:
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")
    user = input("Enter your number of choice:  ")

    if user == "1":
        print("you chose to add a task")
        while True:
            task = input("input task otherwise type quit to quit:  ")
            if task == "quit":
                break
            else:
                print(task)
                user_list.append({"Description":task, "done": False})
                print(f"task {task} added") 

    if user == "2":
        print("you chose to view tasks")
        if not user_list:
            print("No tasks yet")
        else:
            for index, task in enumerate(user_list, start=1):
                status = "[>]" if task["done"] else "[]"
                print(f"{index}, {status} {task['Description']}")

    if user == "3":
        print("You choose to mark a task complete.")
        if not user_list:
            print("No tasks yet")
        else:
            for index, task in enumerate(user_list, start=1):
                status = "[>]" if task["done"] else "[]"
                print(f"{index}, {status} {task['Description']}")

            task_num = int(input("input the task number of your choice"))
            if 1 <= task_num <= len(user_list):
                user_list[task_num - 1]["done"] = True
                print("Task marking complete")
            else:
                print("invalid number boss")

    if user == "4":
        print("You chose to delete a task")
    if user == "5":
        break
    else:
        print("Invalid choice")


