""" Unit Testing for Practical Task - OOP Modules  """


import unittest
from datetime import datetime
from logic import Task

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Title", "Description", datetime.now())
        self.assertEqual(task.title, "Title")
        self.assertEqual(task.description, "Description")
        self.assertFalse(task.completed)  # Task should initially be incomplete


    def test_mark_as_done(self):
        task = Task("Title", "Description", datetime.now())
        task.mark_as_done()
        self.assertTrue(task.completed)


    def test_mark_as_not_done(self):
        task = Task("Title", "Description", datetime.now())
        task.mark_as_done()  # Mark as done first
        task.mark_as_not_done()
        self.assertFalse(task.completed)


    def test_set_due_date(self):
        task = Task("Title", "Description", datetime.now())
        due_date = datetime(2024, 5, 30)
        task.set_due_date(due_date)
        self.assertEqual(task.due_date, due_date)




if __name__ == '__main__':
    unittest.main()
