import functions

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()  # Delete useless spaces
    # We change the structure from match to if condition
    if user_action.startswith('add'):
        user_action = user_action.strip()
        while user_action[3:] == '':
            user_action = input(
                "You enter an empty string. try again. Type add, show, edit, complete or exit: ").strip()
        # We need to append "todo" to our file list
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todo = todo.capitalize()
        todos.append(todo)

        # We do not assign this funtion to variable only call because this funtion do not return any output
        functions.write_todos('files/todos.txt', todos)

    elif user_action.startswith('show'):
        # We execute code in the 'show' case only opening and reading txt file
        todos = functions.get_todos()

        #  Another way to remove "\n" from end of list items
        #  todos = [item.strip('\n') for item in todos] - list comprehension

        for index, todo in enumerate(todos):
            todo = f"{index + 1}) {todo}"
            print(todo, end='')

    elif user_action.startswith('edit'):
        try:
            todos = functions.get_todos()

            for index, todo in enumerate(todos):
                todo = f"{index + 1}) {todo}"
                print(todo, end='')
            # We use only characters after 'edit'
            edit_num = int(user_action[4:])
            while True:

                if user_action.lower() == "exit":
                    break

                if 0 < int(edit_num) <= len(todos):
                    new_todo = input("Enter new todo: ")
                    new_todo = new_todo.capitalize()
                    todos[int(edit_num) - 1] = new_todo + '\n'
                    break

                edit_num = input("The value out of list. Enter correct number:  ")
        except ValueError:
            print('Your input is not valid. correct form example :  "edit + space + number of todo" .')
            continue

        # Overwriting new todos items using 'w' mode
        functions.write_todos('files/todos.txt', todos)

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            print(f'{todos[number - 1]} was delete from the list!')
            todos.pop(number - 1)

            functions.write_todos('files/todos.txt', todos)
        except IndexError:
            print('Your number out of range. please try again...')
            continue
    elif user_action.startswith('exit'):
        # print(*todos, sep='\n')
        break
    else:
        print("Command is not valid!")
