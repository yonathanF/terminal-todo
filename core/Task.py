'''
Holds the task class and related functions. The task class defines
a base class for all tasks (might extend in the future).
It define the following attributes:
     * list that contains all tags for the task,
     * list for all projects the task is related to,
     * title string,
     * due date
     * priority level on a scale of 1 to 4
     * creation date, auto populated
'''

from datetime import datetime
from enum import Enum


class Priority(Enum):
    ''' a simple enum for priorities to avoid using strings or ints '''
    high = 1
    med = 2
    low = 3


def convert_to_datetime(string_date):
    ''' takes a string date and returns an equivalent datetime object '''

    today = datetime.today()
    day = today.weekday()
    month = today.month

    return str(month)


class Task:
    ''' the main task class, see description above '''

    def __init__(self, title, due_date, priority_level, tags, projects):
        self.id = -1
        self.title = title
        self.due_date = due_date
        self.tags = tags
        self.projects = projects
        self.priority_level = priority_level
        self.creation_date = datetime.now()

    def __str__(self):
        ''' prints the task in a nice format'''
        string = str(self.id) + "\t" + self.title + "\t" + str(
            self.due_date) + "\t" + str(self.creation_date) + "\t" + str(
                self.priority_level.name) + "\t"

        # add the tags and projects
        for tag in self.tags:
            string += '@' + str(tag) + ' '

        # add spacing b/n tags and project
        string += "\t"

        for project in self.projects:
            string += '#' + str(project) + ' '

        return string
