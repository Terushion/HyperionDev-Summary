# controller/business_logic.py
from logic import Task
from view import app_name, main_menu, edit_task_menu
from datetime import datetime
from datetime import date
import time

# Use consistent date format
now = datetime.now().date()

# Define a fixed old date for task examples
old_date = datetime(2024, 5, 18).date()


# Add a few instances of a Task to the incomplete list
incomplete = [
    Task(
        "Check Diary",
        "I need to check my diary to plan roughly what I want to"
        " do for the next couple of weeks.",
        old_date,
    ),
    Task(
        "Complete Task 18",
        "I need to finish Task 18 on the Hyperion bootcamp (OOP - Modules).",
        old_date,
    ),
    Task("Daily task", "Do 50 pushups a day", old_date),
]


# Add 1 or 2 instances of a Task to the finished list
finished = [Task("Sleep pattern", "Sleep for 8 hours on Monday.", old_date)]


def view_all_tasks(tasks):
    """
    Argument: The chosen album to display (either album1 or album2 list)
    Return: Displays the content of the chosen album
    """

    print()
    print("\nHere are all of your current Tasks:\n")
    for idx, item in enumerate(tasks):
        print(
            f"{idx+1}.\n"
            f"Title: {item.title}\n"
            f"Due date: {item.due_date}\n"
        )

    next_option()


def next_option():
    view_choice = input(
        "\nWould you like to:\n"
        "1. Select a task\n"
        "2. Head back to the main menu?\n"
        "\nSelection: "
    )
    print()

    if view_choice == "1":
        index = int(input("Enter task number: "))
        view_task(index)
    elif view_choice == "2":
        _main_menu()
    else:
        print("Invalid choice. Please try again.")
        next_option()


def view_task(index):

    # logic here is to retrieve an object from incomplete list using index
    # The user's choice will be the index as seen below in the while loop
    # By using an 'if not' function, we can say if this is not true essentially

    task = incomplete[index - 1]
    if not task.has_been_selected:
        print("\nTask Details:\n")
        print(task)
        print()

    edit_choice = int(
        input(
            "\nWould you like to:\n"
            "1. Mark this task as finished\n"
            "2. Edit this task\n"
            "3. Delete this task\n"
            "4. View all the tasks again\n"
            "Or\n"
            "5. Go back to the main menu\n"
            "\nSelection: "
        )
    )

    if edit_choice == 1:
        complete_task(task)
        print("Task has been marked as completed. Well done!")
        time.sleep(1)
        view_all_tasks(incomplete)
    elif edit_choice == 2:
        edit(task)
    elif edit_choice == 3:
        incomplete.remove(task)
        print("Task has been deleted.")
    elif edit_choice == 4:
        view_all_tasks(incomplete)
    elif edit_choice == 5:
        _main_menu()
    else:
        print("Oops - Error: invalid choice.")
        view_task(index)


def view_old_tasks():

    print("\nFinished Tasks:\n")
    for idx, item in enumerate(finished):
        print(
            f"{idx+1}.\n"
            f"Title: {item.title}\n"
            f"Date of completion: {item.due_date.strftime('%d-%m-%Y, %H:%M:%S')}\n"
        )


def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date_str = input("Enter due date (DD/MM/YYYY) (optional): ")
    due_date = (
        datetime.strptime(due_date_str, "%d/%m/%Y") if due_date_str else None
    )
    task = Task(title, description, due_date)
    incomplete.append(task)
    print("\nYour task has created successfully!")
    view_choice = input(
        "Would you now like to view all your current tasks?" " ('y' or 'n'): "
    )
    if view_choice.lower == "y":
        view_all_tasks(incomplete)
    elif view_choice.lower == "n":
        _main_menu()
    else:
        print("Oops - Error: invalid choice.")
        _main_menu()


def complete_task(task):
    if task in incomplete:
        incomplete.remove(task)
        task.mark_as_done()
        finished.append(task)


def anew_task(task):
    if task in finished:
        incomplete.remove(task)
        task.mark_as_not_done()
        incomplete.append(task)


def _main_menu():

    main_menu()
    while True:

        menu_choice = input("Please enter your selection: ")

        if menu_choice == "1":
            view_all_tasks(incomplete)
        elif menu_choice == "2":
            print("\nAdding a task:")
            add_task()
        elif menu_choice == "3":
            print("\nCompleted Tasks:")
            view_old_tasks()
        elif menu_choice.upper() == "Q":
            print("Goodbye, hope to see you again!")
            break  # Exit the loop and end the function
        else:
            print(
                "Oops - invalid choice. I didn't catch that, please enter again."
            )


def start_application():

    app_name()
    _main_menu()


def edit(task, completed=False):
    while True:
        edit_task_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            if not completed:
                complete_task(task)
                print("Task has been marked as completed." " Well done!")
                time.sleep(1)
                _main_menu()
            else:
                anew_task(task)
                print("Task has been edited.")
                time.sleep(1)
                _main_menu()
            break
        elif choice == "2":
            _main_menu()
        else:
            print("Invalid choice. Please try again.")
