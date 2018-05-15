import os
from unittest import TestCase

from core.Scheduler import Scheduler
from core.Task import Priority, Task


class SimpleSchedulerTest(TestCase):
    def test_create_scheduler(self):
        ''' tests ability to create scheduler '''

        task = Task('Study for exam 1', 'Tue', Priority.high,
                    ['@tag1', '@tag2'], ['+project 1', '+project 2'])
        scheduler = Scheduler()
        scheduler.save_to_file(
            task,
            '/home/yonathan/workplace/personal/terminal-todo/data/todo_test.txt'
        )

        with open(
                '/home/yonathan/workplace/personal/terminal-todo/data/todo_test.txt',
                'r') as test_todo:

            content = test_todo.read()
            self.assertTrue('Study for exam 1' in content)
            self.assertTrue('Tue' in content)
            self.assertTrue('tag1' in content)
            self.assertTrue('tag2' in content)
            self.assertTrue('project 1' in content)
            self.assertTrue('high' in content)

        os.remove(
            '/home/yonathan/workplace/personal/terminal-todo/data/todo_test.txt'
        )

    def test_add_task(self):
        ''' tests ability to add a task to schedule '''

        task = Task('Study for exam 1', 'Tue', Priority.high,
                    ['@tag1', '@tag2'], ['+project 1', '+project 2'])
