'''
A small testing server that will hopefully be hosted sometime soon.
OAuth with Todoist requires a callback url, and it doesn't seem like
a good decision (as of now) to put this on the client side. The user
can then just copy past the code and we can grab the token from there.
'''

from flask import Flask, request

app = Flask(__name__)


@app.route('/callback')
def term_callback():
    '''
    A single entry point, for the Todoist api to redirect to.
    It simply prints the code and state
    '''

    # check for error first
    error = request.args.get('error', '')
    if error:
        return "Error: " + error

    code = request.args.get('code')
    state = request.args.get('state')

    if code:
        #get_token(code, state)
        return "<h1> Copy-paste this info: </h1> \n <h3>Code</h3> " + code + "\n<h3> State: </h3> " + state

    return "Something went wrong, see log or terminal."
