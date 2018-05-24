'''
A scheduler for tasks. This is initialized by reading a todo.txt file
and loading all the tasks objects into memory. It provides the ability to
    * add a task
    * edit a task
    * delete a task
    * schedule tasks
    * list tasks by:
        - due date
        - tag
        - project
        - priority
'''


def linear_priority_function(due_date, priority_level, fake_bost=0):
    ''' a function that ranks a task's priority '''
    pass


class Scheduler:
    def __init__(self):
        self.tasks = list()

    def calculate_relative_priority(
            self, priority_function=linear_priority_function):
        '''
        calculates the tasks priority given a priority function
        The function defaults to a a linear function, as a sane option.
        '''
        pass

    def add_task(self, task):
        ''' adds a given task to the schedule '''
        self.tasks.append(task)

    def save_to_file(self, task, todo_file='../data/todo.txt/'):
        '''
        saves the task into a todo list file. Override the default
        param to change the file it writes to.
        '''

        todo_list = open(todo_file, 'a')

        # get the basic info
        csv = task.id + ', ' + task.title + ', ' + str(
            task.due_date) + ', ' + str(task.creation_date) + ', ' + str(
                task.priority_level.name) + ', '

        # add the tags and projects
        for tag in task.tags:
            csv += str(tag) + ', '

        for index, project in enumerate(task.projects):
            csv += str(project)
            if index != len(task.projects) - 1:
                csv += ', '

        # add a new line
        csv += "\n"

        todo_list.write(csv)
        # close the file
        todo_list.close()
