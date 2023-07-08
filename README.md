# ToDo List Assignment

This is a simple assignment to create a ToDo list application that allows users to manage their tasks using the command line interface. The application provides the following functionalities:

- Add/Update items in a list
- List all the todo items in the list with checkboxes indicating completed and incomplete tasks
- Remove an item from the list
- Mark an item as complete or incomplete

## Getting Started

To run and test the ToDo list application, follow the steps below:

### Prerequisites

Make sure you have the following software installed on your system:

- Python (version 3.6 or higher)
- Command-line interface (Terminal, Command Prompt, etc.)

### Installation

1. Clone the repository or download the source code files.
2. Navigate to the project directory in your terminal.

### Usage

1. Open a terminal and navigate to the project directory.
2. Run the following command to start the ToDo list application:

   ```bash
   python todo.py
   ```

   This will start the application and present you with a list of available commands.

3. Use the provided commands to add, update, list, remove, and mark items in the ToDo list.

### Available Commands

The following commands are available for interacting with the ToDo list:

- `add`: Add a new item to the list. You will be prompted to enter the task description.
- `update`: Update an existing item in the list. You will be prompted to enter the task description and the item number to be updated.
- `list`: List all the items in the ToDo list. Completed tasks will be marked with ☑ and incomplete tasks with ☐.
- `remove`: Remove an item from the list. You will be prompted to enter the item number to be removed.
- `complete`: Mark an item as complete. You will be prompted to enter the item number to be marked as complete.
- `incomplete`: Mark a completed item as incomplete. You will be prompted to enter the item number to be marked as incomplete.
- `exit`: Exit the application.

### Example Usage

Here is an example of how you can use the ToDo list application:

```bash
$ python weekly.py
Welcome to the ToDo list application!

Commands:
add - Add a new item
update - Update an item
list - List all items
remove - Remove an item
complete - Mark an item as complete
incomplete - Mark an item as incomplete
exit - Exit the application

> add
Enter the task description: Buy groceries

> add
Enter the task description: Walk the dog

> list
1. Buy groceries ☐
2. Walk the dog ☐

> complete
Enter the item number to mark as complete: 1

> list
1. Buy groceries ☑
2. Walk the dog ☐

> update
Enter the item number to update: 2
Enter the updated task description: Walk the cat

> list
1. Buy groceries ☑
2. Walk the cat ☐

> remove
Enter the item number to remove: 2

> list
1. Buy groceries ☑

> exit
```
