'''
Main driver of the application. It interacts with the user
from the terminal and orchestrates the other functions and
objects to perform needed actions.
'''

import argparse


def main():
    '''
    The entry point of the application.
    '''

    # set the description
    arg_parser = argparse.ArgumentParser(
        prog="term_todoist",
        description='A simple terminal client for Todoist that\
        supports all functionality of the web application.')

    # add task
    arg_parser.add_argument(
        '-a',
        type=str,
        help="Add a task. Add time near the end\
            with a -t [usual string time]")

    # edit task
    arg_parser.add_argument(
        '-e',
        type=str,
        help="Edit a task. Enter task id followed by the change")

    # list tasks a label
    arg_parser.add_argument(
        '-ll', type=str, help="List all tasks with these tag/s")

    # list tasks with project
    arg_parser.add_argument(
        '-lp', type=str, help="List all tasks under this project")

    # auth argument
    arg_parser.add_argument(
        '-auth',
        type=bool,
        help="Go through the OAuth process. Only need to do it once.")

    args = arg_parser.parse_args()


if __name__ == "__main__":
    main()
