'''
A wrapper for the Todoist Rest API to avoid coupling
It provides a function for every endpoint [hopefully]
'''

import json
from collections import namedtuple

import requests

# a representation of a task
Task = namedtuple(
    'Task',
    'project_name content date_string indent priority lables completed')


class API:
    '''
    The wrapper class for the api provides the REST endpoints
    as methods. Decided to put it in a class because there is
    enough data shared among the methods, such as token etc
    '''

    def __init__(self, token, api_url):
        self.token = token
        self.api_url = api_url
        self.projects = self.get_project_names()
        self.labels = self.get_label_names()
        self.header = {"Authorization": "Bearer %s" % self.token}

    def get_project_names(self):
        '''
        Iterates through all the projects and forms a dictionary
        of id to project name. Used for later to map in reverse direction
        '''

        # make a request for all projects
        # returns name, id, order, indent, etc
        projects_request = requests.get(
            self.api_url + "/projects", headers=self.header)

        # convert it to a dict
        projects_dict = json.loads(projects_request.json())

        # iterate through it and create the mapping
        for project in projects_dict:
            self.projects[project['id']] = project['name']

    def get_label_names(self):
        '''
        Iterates through all the labels in the user account and
        creates a dictionary that maps from label ids to label name.
        Also used for reverse lookup from id to name.
        '''

        # make a request for all labels
        # returns name, id, order
        labels_request = requests.get(
            self.api_url + "/labels", headers=self.header)

        # convert it to a dict
        labels_dict = json.loads(labels_request.json())

        # iterate through it and create the mapping
        for label in labels_dict:
            self.labels[label['id']] = label['name']

    def convert_task(self, task_json):
        '''
        Takes in a task in a json format and returns a
        named tuple with all ids converted to human readable names
        '''

        # get task project name using pre populated dict
        task_project = self.projects[task_json["project_id"]]

        # get all the label ids and iterate through them
        task_labels = task_json["label_ids"]

        # this replaces the ids by their names one by one
        for label, _ in enumerate(task_labels):
            task_labels[label] = self.labels[task_labels[label]]

        # create a tuple for clean syntax and return it
        task = Task(task_project, task_json["content"],
                    task_json["due"]["string"], task_json["indent"],
                    task_json["priority"], task_labels, task_json["completed"])

        return task

    def get_task(self, task_id):
        '''
        Gets a task by the id
        '''

        # make a request for the resources
        task_request = requests.get(
            self.api_url + "/tasks/" + task_id, headers=self.header)

        # get the data as a json
        task_json = json.loads(task_request.json())

        # convert it to a named tuple
        task = self.convert_task(task_json)

        return task
