def get_todos(filepath='todos.txt'):
    """Read a Text File and return the list of todo items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath='todos.txt'):
    """Write the todo items in the list"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)