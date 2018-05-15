'''
Holds the task class and related functions. The task class defines
a base class for all tasks (might extend in the future).
It define the following attributes:
     list that contains all tags for the task,
     list for all projects the task is related to,
     title string,
     due date
     priority level on a scale of 1 to 4
     creation date, auto populated
'''


class Task:
    ''' the main task class, see description above '''

    def __init__(self, title, due_date, priority_level, tags, projects):
        self.title = title
        self.due_date = due_date
        self.tags = tags
        self.projects = projects
        self.priority_level = priority_level

    def save_to_file(self, todo_file='../data/todo.txt/'):
        '''
        saves the task into a todo list file. Override the default
        param to change the file it writes to.
        '''

        todo_list = open(todo_file, 'a')

        # get the basic info
        csv = self.title + ', ' + str(self.due_date) + ', ' + str(
            self.priority_level)

        # add the tags and projects
        for tag in self.tags:
            csv += str(tag) + ', '

        for project in self.projects:
            csv += str(project) + ', '
