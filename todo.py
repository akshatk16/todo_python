from datetime import date
import os
import sys


def addTodo(todoItem):
    # ✓ add a single todo
    # ✓ show error message when add is not followed by a todo
    # ✓ add multiple todos
    if os.path.isfile('todo.txt'):
        with open("todo.txt") as f:
            lines = f.readlines()  # read existing todos
        lines.insert(0, todoItem + "\n")  # add new todo
        with open("todo.txt", "w") as f:
            f.writelines(lines)  # write new+old todos
    else:
        with open("todo.txt", 'w') as f:  # new file for first todo
            f.write(todoItem + '\n')
    print(f'Added todo: "{todoItem}"')  # completion message


def printTodos():
    # ✓ list todos in reverse order (added latest first)
    # ✓ list when there are no remaining todos
    if os.path.isfile('todo.txt'):
        with open("todo.txt") as f:
            lines = f.readlines()  # read existing todos
        numOfTodos = len(lines)  # number of existing todos
        if numOfTodos < 1:  # no todos
            print("There are no pending todos!")
        for line in lines:
            # print in specified format without '\n' character
            print(f'[{numOfTodos}] {line[:-1]}')
            numOfTodos -= 1  # decrement index
    else:
        print("There are no pending todos!")  # todo file does not exist yet


def delFromList(todoNum):
    # ✓ delete a todo
    # ✓ delete todos numbered 3, 2 & 1
    # ✓ delete first todo item 3 times
    # ✓ delete non-existent todos
    # ✓ delete does not have enough arguments
    if todoNum <= 0:
        print(f'Error: todo #{todoNum} does not exist. Nothing deleted.')
    elif os.path.isfile('todo.txt'):
        with open("todo.txt") as f:
            lines = f.readlines()  # read existing todos
        numOfTodos = len(lines)
        if todoNum > numOfTodos:  # outOfBounds todoNum
            print(f'Error: todo #{todoNum} does not exist. Nothing deleted.')
        else:
            del lines[todoNum - 1]  # delete from todo file
            with open("todo.txt", 'w') as f:
                f.writelines(lines)  # write rest todos to file
            print(f'Deleted todo #{todoNum}')  # completion message
    else:
        print(f'Error: todo #{todoNum} does not exist. Nothing deleted.')


def markDone(todoNum):
    # ✓ mark a todo as done
    # ✓ mark as done a todo which does not exist
    # ✓ mark as done without providing a todo number
    ymd = "%Y-%m-%d"  # format for date.today()
    if todoNum <= 0:
        print(f'Error: todo #{todoNum} does not exist.')
    elif os.path.isfile('todo.txt'):
        with open("todo.txt") as f:
            lines = f.readlines()  # read existing todos
            numOfTodos = len(lines)
            if todoNum > numOfTodos:  # outOfBounds todoNum
                print(f'Error: todo #{todoNum} does not exist.')
                return
            else:
                todoDone = lines[todoNum - 1]  # todo to be marked done
                del lines[todoNum - 1]  # delete from todo file
                with open("todo.txt", 'w') as f:
                    f.writelines(lines)  # write rest todos to file
        if os.path.isfile('done.txt'):
            with open("done.txt") as f:
                lines = f.readlines()  # read existing done todos
            # insert done todo in required format
            lines.insert(0,
                         f'x {date.today().strftime(ymd)} {todoDone}')
            with open("done.txt", "w") as f:
                f.writelines(lines)  # write done todos back to file
        else:
            with open("done.txt", 'w') as f:  # new file for first done todo
                # insert done todo in required format
                f.write(f'x {date.today().strftime(ymd)} {todoDone}')
        print(f'Marked todo #{todoNum} as done.')  # completion message
    else:
        # todo file does not exist yet
        print(f'Error: todo #{todoNum} does not exist.')


def helpMenu():
    # ✓ prints help when no additional args are provided
    # ✓ prints help
    helpItems = """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
    print(helpItems)


def todoReport():
    # ✓ report pending & completed todos (219 ms)
    p = 0  # default for no pending
    if os.path.isfile('todo.txt'):
        with open('todo.txt') as f:
            lines = f.readlines()  # read existing todos
            p = len(lines)  # number of pending todos
    c = 0  # default for no completed
    if os.path.isfile('done.txt'):
        with open('done.txt') as f:
            lines = f.readlines()  # read existing done todos
            c = len(lines)  # number of completed todos
    ymd = "%Y-%m-%d"  # format for date.today()
    # print message in required format
    print(f'{date.today().strftime(ymd)} Pending : {p} Completed : {c}')


def main():
    # check if no arguments passed
    if len(sys.argv) == 1:
        helpMenu()

    # check if add argument passed
    elif sys.argv[1] == 'add':
        if len(sys.argv) == 3:
            addTodo(sys.argv[2])
        else:
            print("Error: Missing todo string. Nothing added!")

    # check if ls argument passed
    elif sys.argv[1] == 'ls':
        printTodos()

    # check if del argument passed
    elif sys.argv[1] == 'del':
        if len(sys.argv) == 3:
            delFromList(int(sys.argv[2]))
        else:
            print("Error: Missing NUMBER for deleting todo.")

    # check if done argument passed
    elif sys.argv[1] == 'done':
        if len(sys.argv) == 3:
            markDone(int(sys.argv[2]))
        else:
            print("Error: Missing NUMBER for marking todo as done.")

    # check if help argument passed
    elif sys.argv[1] == 'help':
        helpMenu()

    # check if report argument passed
    elif sys.argv[1] == 'report':
        todoReport()

    # prompt help comman if unknown argument passed
    else:
        print("Unknown argument. Use 'help' for a list of available commands")


if __name__ == "__main__":
    main()
