'''
Handles OAuth with Todoist. It will store the token in a json file once the process
is completed.
'''

import uuid
import webbrowser

import requests

# api info
CLIENT_ID = "9662f098a73140eebc7f1fdb9efac61f"
CLIENT_SECRET = "df93a09ff8ec49b8beba8e6a8e23f5f6"
AUTH_URL = "https://todoist.com/oauth/authorize"
TOKEN_URL = "https://todoist.com/oauth/access_token"


def get_token(code, state):
    '''
    Exchanges the code for a token. Step 2 of 2.
    '''
    # uuid for state
    state = uuid.uuid4().hex


def get_code(state):
    '''
    Makes a request for authorization. Step 1 of 2, see
    https://developer.todoist.com/sync/v7/#oauth
    '''

    # permissions
    scope = "task:add, data:read, data:read_write, data:delete,\
            data:delete, project:delete"

    # form the data
    data = "?scope=" + scope + "&client_id=" + CLIENT_ID + "&state=" + state

    # open the auth link in the default browser
    webbrowser.open(AUTH_URL + data)


get_code("234")
