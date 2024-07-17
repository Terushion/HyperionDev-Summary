# model/task.py
from datetime import datetime


class Task:

    def __init__(self, title, description, due_date=None):
        self.title = title
        self.description = description
        self.completed = False
        self.creation_date = (
            datetime.now()
        )  # Set creation date to current date and time
        self.due_date = due_date
        self.has_been_selected = False

    def mark_as_done(self):
        self.completed = True

    def mark_as_not_done(self):
        self.completed = False

    def __str__(self):
        status = "Done" if self.completed else "Not Done"
        due_date = (
            self.due_date.strftime("%d-%m-%Y") if self.due_date else "None"
        )
        return (
            f"Title: {self.title}   |   Status: {status}\n"
            f"Due: {due_date}\n"
            f"Description:\n        {self.description}"
        )

    def set_due_date(self, due_date):
        self.due_date = due_date

    def get_due_date(self):
        return self.due_date

    def is_overdue(self):
        if self.due_date and self.due_date < datetime.now():
            return True
        return False
