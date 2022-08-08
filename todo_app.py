f = open("tasks.txt", "a")
# Todo List Exercise

# Create an interactive, text-based todo list that has the following features:

# - A user can add todos by entering them into the prompt | Done
# - A user can complete todos by entering the todo’s corresponding number 
# - A user can view a help screen by typing ‘h’ or ‘help’
# - A user can quit by typing ‘q’ or ‘quit

print("*" * 40)
print("The Todo App")
print("*" * 40)
# i = 0
# todo = []
# todo_tasks = []

# print("To add a ToDo simply type the todo and press enter.")
# print("To mark a ToDo as done type the item's relevant number.")
# while todo != "q":
#     todo = input("Please enter your new ToDo: ")
#     todo_tasks.append(todo)
#     print(todo)
#     print(todo_tasks)
#     for todo_task in todo_tasks:
#         i+=1
#         print(f"{i}. {todo_task}")

#####################
# Course solution
todos = []
finished = []

while True:
    # This is where I got stuck when working on my own solution. Make the tasks part of a range. 
    for i in range(len(todos)):
        print(f"* {i+1}. {todos[i]}")
    print("*" * 45)
    print("Enter a command. Type 'h' for help:")
    command = input("> ")
    if command == "q" or command == "quit":
        f.close()
        break
    elif command == "h" or command == "help":
        print("*" * 35)
        print("Command options: ")
        print("Simply type in your task and press enter.")
        print("To delete a task just type the task number and enter.")
        print("To exit the app press 'q' or type 'quit' and enter.")
        print("*" * 35)
    elif command.isnumeric():
        i = int(command) -1
        if i >= len(todos):
            print(f"{i + 1} does not exist yet! ")
        else:
            # remove the completed task by popping it. Take what is returned and add it to the completed list
            completed_task = todos.pop(i)
            finished.append(completed_task)
    else: 
        todos.append(command)
        f.write(command + "\n")

print("Tata For Now!")
print(f"We completed {len(finished)} tasks today: ")
for todo in finished:
    print(f"* {todo}")
