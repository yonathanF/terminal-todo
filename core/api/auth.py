'''
Handles OAuth with Todoist. It will store the token in a json file once the process
is completed.
'''

import webbrowser

import requests

from config import *


def write_token_to_file(token, token_filename=".token"):
    '''
    Saves the token of the user to disk for later uses
    '''

    if not token:
        raise Exception("Token is empty")

    with open(token_filename, 'w') as token_file:
        token_file.write(token + "\n")


def load_token_from_file(token_filename=".token"):
    '''
    Reads in the token from file once the auth process is completed
    for subsquent reuses
    '''

    with open(token_filename, 'r') as token_file:
        token = token_file.readline()

    if token:
        return token

    raise Exception("You need to authenticate at least once")


def get_token(code):
    '''
    Exchanges the code for a token. Step 2 of 2.
    '''
    # required data
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code
    }

    # make the request
    token_request = requests.post(TOKEN_URL, data)
    token = token_request.json()['access_token']

    return token


def get_code(state):
    '''
    Makes a request for authorization. Step 1 of 2, see
    https://developer.todoist.com/sync/v7/#oauth
    '''

    # permissions, request everything
    scope = "task:add, data:read, data:read_write, data:delete,\
            data:delete, project:delete"

    # form the data
    data = "?scope=" + scope + "&client_id=" + CLIENT_ID + "&state=" + state

    # open the auth link in the default browser
    webbrowser.open(AUTH_URL + data)

    # get the code and state from the user
    code = input("Enter the code: ")
    check_state = input("Enter the state: ")

    return code, check_state
