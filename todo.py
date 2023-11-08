
# To-Do list Project #

tasks = [] # Empty list to store tasks

# Defined Functions

def show_help(task): # Function to provide commands list
    print("Available commands:")
    for command in commands:
        print(f"- {command}")

def create_task(task): # Function to create a task
    if task.strip():
        tasks.append(task)  # Add the task to the list
        print(f"Task created: {task} \n")
    else:
        print("Task creation failed. To create a task, use the 'create' command followed by a task description, as shown below: ")
        print("EXAMPLE: create Buy groceries \n")

def delete_task(task): # Function to delete a task
    if not task:
        print("Please specify the task to delete it. \n")
        return  # Exit the function if no task is provided

    if task in tasks: # If task is valid, then remove task and display message, else display error message
        tasks.remove(task)
        print(f"Task deleted: {task}. \n")
    else:
        print(f"Task '{task}' not found.\n")


def list_tasks(task): # Function to list all tasks
    print("Task List: \n")
    
    if not tasks:  # Check if there are no tasks
        print("No tasks found. \n")
    else:
        for index, task_description in enumerate(tasks, start=1): # Iterate through tasks with index, starting at 1
            print(f"{index}. {task_description} \n")

def quit_program(task): # Function to quit the program
    print("Exiting program. Bye-Bye!")
    exit()

# Dictionary to map commands to functions

commands = {
    'quit': quit_program,
    'help': show_help,
    'create': create_task,
    'delete': delete_task,
    'list': list_tasks,
}

# Main program loop

print("//////////////////////////////////////////")
print("Welcome to the Python To-Do list Program!")
print("////////////////////////////////////////// \n")

while True:
    user_input = input("Enter a command (Type 'help' to see a list of commands): ").strip().lower() # Prompt input and remove leading/trailing whitespace, and convert to lowercase

    parts = user_input.split(' ', 1) # Split input into 'command' and 'task'
    command = parts[0] # Extract command
    task = parts[1] if len(parts) > 1 else '' # Extract task (only if present)

    if command in commands:  # If command is valid, execute correct function
        commands[command](task) # Input error handler
    else:
        print("Invalid command. Type 'help' for a list of available commands. \n")
