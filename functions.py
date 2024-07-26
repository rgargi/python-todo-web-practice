import os

FILEPATH = "tasks.txt"

if not os.path.exists(FILEPATH):
    with open(FILEPATH, "w") as f:
        print("File Created")
        pass

# writelines() doesn't add a new line -> so we added one
# readlines() adds a new line automatically
# everytime we are reading it we add a new line
# then we add another when we save it using the writelines() with added new line
# (print statement also displays a new line)
# therefore using read() which doesn't add newlines
# we could also use readlines() and strip the extra "\n"

def get_tasks(filepath=FILEPATH):
    """Get tasks from the the file."""
    with open(filepath, "r") as f:
        tasks_data = f.read().splitlines()
    return tasks_data

def update_file(tasks_list, filepath=FILEPATH):
    """ Update the file with changes. Run after adding a new task, 
    editing a task, and deleting a completed task."""
    update_done = 0
    try:
        with open(filepath, "w") as f:
            f.writelines("%s\n" % t for t in tasks_list)
        update_done = 1
    except UnicodeEncodeError as err:
        update_done = 0
        print("You entered characters which cannot be encoded.")
    return update_done
                                                                              
def addtask(task):
    tasks = get_tasks()
    tasks.append(task)
    if update_file(tasks) == 1:
        msg = "Task added"
    else:
        msg = "Task couldn't be added"
    return msg

def completetask(index):
    tasks = get_tasks()
    x_task = tasks.pop(index)
    update_file(tasks)
    msg = f"'{x_task}' was removed"
    return msg