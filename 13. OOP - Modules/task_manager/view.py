# view/ui.py
import time



def app_name():
    print("Task Manager\n"
          "Welcome back User!\n")



def main_menu():


    menu = "\nMain Menu\n"
    time.sleep(1)
    menu += "Please select an option below:\n\n"
    menu += "1. View all tasks\n"
    menu += "2. Add Task\n"
    menu += "3. View your finished tasks\n\n"
    menu += "Q. Quit application\n"
    print(menu)




def edit_task_menu(completed=False):
    
    edit_menu = "\nEdit Task Menu:\n"
    edit_menu += "1. Mark as Done\n" if not completed else "1. Mark as Not Done\n"
    edit_menu += "2. Go Back to Main Menu\n"
    print(edit_menu)