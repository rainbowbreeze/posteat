"""
Conventions:
 Base APIs are exposed using the address https://_hostname_/posteatbot/api/v1.0/

 Authorization code is passed in the X-Authorization field of the payload (or headers)
"""

from datetime import date

from flask import Flask, request

"""
# Added to prevent ImportError: No module named 'posteat'
#  when this file is in not in the same module structure that
#  the main class to launch
# https://stackoverflow.com/a/9806045/584134
# Please also note the difference between append and insert
import os
import inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
os.sys.path.insert(0, parent_dir)
"""
# ---
from posteat.posteat import PostEat

app = Flask(__name__)  # create the application instance :)
app.config.from_object(__name__)  # load config from this file , flaskr.py

# Creates an instance of the main module
posteat = PostEat(debug=True)

# Basic address for all the API calls
BASIC_ADDRESS = '/posteatbot/api/v1.0'

@app.route("/")
def hello_world():
    return 'Hello World!'


@app.route('{}/getmenu'.format(BASIC_ADDRESS), methods=['GET'])
def echo_message():
    print('***************************')
    print(request.headers)
    print('***************************')
    print(request)
    print('***************************')
    print(request.get_json())
    print('***************************')
    # Finds today's date
    today = date.today()
    year = today.year
    month = today.month
    day = today.day
    menu = posteat.get_menu(year, month, day)
    if menu is None:
        return "Nessun menu trovato per il giorno {}".format(get_month_name(today))
    else:
        return 'Menu del giorno {}:\n{}'.format(
            get_month_name(today),
            menu
        )

def get_month_name(today):
    return today.strftime('%a %d %B')



def extract_auth(response):
    """Extracts auth header from the call"""
    pass

# As per PythonAnywhere documentation, "you should make sure your code
# does *not* invoke the flask development server with app.run(), as it
# will prevent your wsgi file from working.

if __name__ == "__main__":
    app.run()


