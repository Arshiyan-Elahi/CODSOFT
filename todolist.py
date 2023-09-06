import time
print("\t\tTODO - LIST \n 1.INSERT  \n 2.SEARCH \n 3.DELETE \n 4.UPDATE \n 5.EXIT")
task_list = []


while True:
    program_choice = input("Which operation do you want to perform (1/2/3/4/5): ")
    print("\t\tTODO - LIST \n 1.INSERT  \n 2.SEARCH \n 3.DELETE \n 4.UPDATE \n 5.EXIT")

    if program_choice == "1":
        ## INSERT ##
        while True:
            choice = input("Enter Schedule, press Y; otherwise, press N: ")

            if choice.upper() == "Y":
                task = input("Enter task for Schedule: ")
            else:
                break

            named_tuple = time.localtime()  # get struct_time
            add_time = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

            task_data = {
                "task": task,
                "add_time": add_time
            }

            task_list.append(task_data)

        ## Print all tasks ##
        print("Final Tasks:")
        for task_data in task_list:
            print("Task:", task_data["task"])
            print("Time:", task_data["add_time"])
            print()

    ## SEARCH ##
    elif program_choice == "2":
        search_task = input("Enter the task name you want to search: ")
        found = False

        for task_data in task_list:
            if task_data["task"] == search_task:
                print("Task:", task_data["task"])
                print("Time:", task_data["add_time"])
                found = True
                break

        if not found:
            print("Task not found.")

    ## DELETE ##
    elif program_choice == "3":
        del_task = input("Enter the task which you want to delete: ")
        tasks_to_remove = []

        for task_data in task_list:
            if task_data["task"] == del_task:
                tasks_to_remove.append(task_data)

        for task_data in tasks_to_remove:
            task_list.remove(task_data)

    ## UPDATE ##
    elif program_choice == "4":
        update_task = input("Enter task you want to update: ")
        found = False

        for task_data in task_list:
            if task_data["task"] == update_task:
                new_task = input("Enter the updated task: ")
                task_data["task"] = new_task
                found = True
                break

        if not found:
            print("Task not found for updating.")

        print(task_list)    

    ## EXIT ##
    elif program_choice == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")

print("Program ended.")
