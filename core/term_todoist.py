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
        description=
        'A simple terminal client for Todoist that supports all functionality of the web application.'
    )

    # add task argument
    arg_parser.add_argument(
        'integer', metavar='N', type=int, nargs="+", help="some help")

    args = arg_parser.parse_args()


if __name__ == "__main__":
    main()
