"""
Conventions:
 Base APIs are exposed using the address https://_hostname_/posteatbot/api/v1.0/

 Authorization code is passed in the X-Authorization field of the payload (or headers)
"""
import json
import locale
from datetime import date

from flask import Flask, request, make_response

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

# Set locale. Check available on local machine with locale -a
try:
    locale.setlocale(locale.LC_ALL, 'it_IT')
except:
    pass

# Creates an instance of the main module
posteat = PostEat(debug=True)

# Basic address for all the API calls
BASIC_ADDRESS = '/posteatbot/api/v1.0'

@app.route("/")
def hello_world():
    return 'Hello World!'


@app.route('{}/getmenu'.format(BASIC_ADDRESS), methods=['GET'])
def api_getmenu():
    """Returns the today's menu to visualize on a webpage"""
    response = get_menu(request)
    return response.replace('\n', '<BR>')  # Suitable for visualization in a web browser


@app.route('{}/apiai_webhook'.format(BASIC_ADDRESS), methods=['POST'])
def apiai_webhook():
    """Returns the today's menu to interact with API.ai"""
    # See example at https://github.com/api-ai/apiai-weather-webhook-sample/blob/master/app.py
    #  https://docs.api.ai/docs/webhook

    print("---- API.ai Request headers")
    print(request.headers)
    apiai_req = request.get_json(silent=True, force=True)
    print("---- API.ai Request")
    print(json.dumps(apiai_req, indent=4))

    apiai_res = process_apiai_request(apiai_req)
    apiai_res = json.dumps(apiai_res, indent=4)
    print("---- API.ai Response")
    print(apiai_res)

    res = make_response(apiai_res)
    res.headers['Content-Type'] = 'application/json'
    return res


def process_apiai_request(apiai_req):
    """Process API.ai request and return a compatible API.ai result"""
    if apiai_req.get('result').get('action') != 'show_menu':
        return {}

    menu_text = get_menu(request)
    apiai_res = {
        'speech': menu_text,
        'displayText': menu_text,
        # "data": data,
        # "contextOut": [],
        'source': 'apiai-posteatbot'
    }
    return apiai_res


def get_menu(req):
    """Finds menu for today"""
    # Finds today's date
    today = date.today()
    year = today.year
    month = today.month
    day = today.day
    menu = posteat.get_menu(year, month, day)
    if menu is None:
        return "Nessun menu trovato per il giorno {}".format(get_month_name(today))
    else:
        return 'Menu del giorno {}\n\n{}'.format(
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


