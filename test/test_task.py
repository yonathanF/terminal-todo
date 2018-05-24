from unittest import TestCase

from core.Task import Priority, Task, convert_to_datetime


class CreateSaveTest(TestCase):
    ''' tests the ability to create and save tasks '''

    def test_create_task(self):
        ''' tests a simple create test '''

        task = Task('Study for exam 1', 'Tue', Priority.high, ['tag1', 'tag2'],
                    ['project 1'])

        task_string = str(task)

        self.assertTrue('Study for exam 1' in task_string)
        self.assertTrue('Tue' in task_string)
        self.assertTrue('tag1' in task_string)
        self.assertTrue('tag2' in task_string)
        self.assertTrue('project 1' in task_string)
        self.assertTrue('high' in task_string)

    def test_time_converted_weekdays(self):
        ''' tests the time converter '''

        mon = convert_to_datetime('mon')
