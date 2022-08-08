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

while True:
    for todo in todos:
        print(f"* {todo}")
    print("*" * 45)
    print("Enter a command. Type 'h' for help:")
    command = input("> ")
    if command == "q":
        break
    else: 
        todos.append(command)

print("Tata For Now!")




        

