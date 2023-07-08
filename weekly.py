""""Initialising an empty to-do list"""
todo_list = []

def print_todo_list() -> None:
    """Function printing to-do list"""
    if len(todo_list) == 0:
        print('The List is Empty!')
    else:
        print("Todo Listttttt:")
        for idx, item in enumerate(todo_list, start=1):
            status = "☑" if item.get("completed") else "☐"
            print(f"{idx}.  {item.get('task', '')} {status}")

def add_item(task) -> None:
    """Function adds an item to to-do list"""
    todo_list.append({'task': task, 'completed': False})
    print(f"'{task}' is added to the to-do list")

def remove_item() -> None:
    """Function removes an item to to-do list"""
    print_todo_list()
    index = int(input('Enter the index of the item to be removed: '))
    removed_item = todo_list.pop(index - 1)
    print(f"'{removed_item['task']}' is removed from the to-do list")

def mark_complete() -> None:
    """Function marks an item completed in to-do list"""
    print_todo_list()
    index = int(input('Enter the index you want to mark: '))
    if index < 1 or index > len(todo_list):
        print("Invalid item index.")
    else:
        todo_list[index - 1]['completed'] = True
        print(f"Marked item '{todo_list[index - 1]['task']}' as complete.")
    print_todo_list()

def mark_incomplete() -> None:
    """Function marks an item incompleted in to-do list"""
    print_todo_list()
    index = int(input('Enter the index you want to unmark: '))
    if index < 1 or index > len(todo_list):
        print("Invalid item index.")
    else:
        todo_list[index - 1]['completed'] = False
        print(f"Marked item '{todo_list[index - 1]['task']}' as incomplete.")
    print_todo_list()

def update_task() -> None:
    """Function updates an item to to-do list"""
    print_todo_list()
    index = int(input("Enter the index of the task to update: "))
    if index < 1 or index > len(todo_list):
        print("Invalid item index.")
    else:
        new_task = input("Enter the new task description: ")
        todo_list[index - 1]["task"] = new_task
        print("Task updated successfully.")
    print_todo_list()

def main():
    """This is the main function"""
    while True:
        print('\nPress the key to perform the function')
        print('1. List of all items.')
        print('2. Add an item.')
        print('3. Remove an item.')
        print('4. Mark the task completed')
        print('5. Un-Mark the a task')
        print('6. Update a task')
        print('7. Exit')
        choice = input('Enter 1-7: ')

        if choice == '1':
            print('\nTODO LIST:')
            print_todo_list()
        elif choice == '2':
            task = input('Enter the task to be added: ')
            add_item(task)
        elif choice == '3':
            remove_item()
        elif choice == '4':
            mark_complete()
        elif choice == '5':
            mark_incomplete()
        elif choice == '6':
            update_task()
        elif choice == '7':
            print('The Program has ended!!')
            break
        else:
            print('Invalid choice, please select (1-7)')



if __name__ == "__main__":
    main()
    